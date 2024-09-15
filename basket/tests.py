from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Product, Customer, Order, OrderItem, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Basket, BasketItem


class BasketViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test categories
        category1 = Category.objects.create(name="Fiction")
        category2 = Category.objects.create(name="Non-Fiction")
        category3 = Category.objects.create(name="Science Fiction")

        # Create a dummy image file for testing
        dummy_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )

        # Create test products
        cls.product1 = Product.objects.create(
            name="Test Product 1",
            description="A great book on testing in Django.",
            price=19.99,
            image=dummy_image,
            author="John Doe"
        )
        cls.product1.category.add(category1, category2)  # Adding multiple categories

        cls.product2 = Product.objects.create(
            name="Test Product 2",
            description="An amazing guide to Django.",
            price=29.99,
            image=dummy_image,
            author="Jane Smith"
        )
        cls.product2.category.add(category2)

        cls.product3 = Product.objects.create(
            name="Test Product 3",
            description="A science fiction masterpiece.",
            price=15.99,
            image=dummy_image,
            author="Isaac Asimov"
        )
        cls.product3.category.add(category3)
        # Setup a client, create a user, customer
        cls.client = Client()
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.customer = Customer.objects.create(user=cls.user)

    def test_authenticated_user_basket_view(self):
        # Log user in
        self.client.login(username='testuser', password='12345')
        # Test basket view for an authenticated user
        basket = Basket.objects.create(user=self.user)
        BasketItem.objects.create(
            basket=basket,
            product=self.product1,
            quantity=1,
        )
        response = self.client.get(reverse('basket:basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket.html')
        # Check the basket show the correct item
        self.assertContains(response, self.product1.name)

    def test_anonymous_user_basket_view(self):
        # Make sure no user is logged in
        self.client.logout()
        # Manually set the session to simulate an existing basket item
        session = self.client.session
        session['basket'] = {str(self.product1.id): 2}  # 2 quantities of product 1
        session.save()
        response = self.client.get(reverse('basket:basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket.html')
        # Check the basket show the correct item
        self.assertContains(response, self.product1.name)

    def test_add_to_basket_authenticated_user(self):
        # Log user in
        self.client.login(username='testuser', password='12345')
        # Define the URL and quantity for adding to basket
        url = reverse('basket:add-to-basket', kwargs={'product_id': self.product2.id})
        data = {'quantity': 1}

        # Make a POST request as an anonymous user
        response = self.client.post(url, data, follow=True)

        # Verify the user is redirected to the basket page
        self.assertRedirects(response, reverse('basket:basket'))
        self.assertContains(response, self.product2.name)

    def test_add_to_basket_anonymous_user(self):
        # Make sure no user is logged in
        self.client.logout()
        # Define the URL and quantity for adding to basket
        url = reverse('basket:add-to-basket', kwargs={'product_id': self.product2.id})
        data = {'quantity': 1}

        # Make a POST request as an anonymous user
        response = self.client.post(url, data)

        # Verify the user is redirected to the basket page
        self.assertRedirects(response, reverse('basket:basket'))

        # Check the session to see if the product has been added
        session_basket = self.client.session.get('basket', {})

        # Assert that the product has been added to the session basket
        self.assertIn(str(self.product2.id), session_basket)
        self.assertEqual(session_basket[str(self.product2.id)], 1)

    def test_remove_from_basket_anonymous_user(self):
        # Test removing a product from the basket for an anonymous user
        self.client.logout()
        session = self.client.session
        session['basket'] = {str(self.product3.id): 1}
        session.save()
        # Call the view with the item id argument
        response = self.client.post(reverse('basket:remove-from-basket', kwargs={'item_id': self.product3.id}))
        self.assertRedirects(response, reverse('basket:basket'))
        # Assert the item isn't in the session basket
        self.assertNotIn(str(self.product3.id), self.client.session['basket'])

    def test_remove_from_basket_authenticated_user(self):
        # Log user in
        self.client.login(username='testuser', password='12345')
        # Create the basket and item
        basket = Basket.objects.create(user=self.user)
        basket_item = BasketItem.objects.create(basket=basket, product=self.product1, quantity=1)
        # Call the remove view with the item id as the argument
        response = self.client.post(reverse('basket:remove-from-basket', kwargs={'item_id': basket_item.id}))
        self.assertRedirects(response, reverse('basket:basket'))
        # Assert the item doesn't exist in the basket
        self.assertFalse(BasketItem.objects.filter(id=basket_item.id).exists())
