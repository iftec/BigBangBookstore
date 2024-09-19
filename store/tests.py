from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Product, Customer, Order, OrderItem, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone


class StoreViewTests(TestCase):
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
        cls.user = User.objects.create_user(username='test@user.co.uk',
                                            password='12345')
        cls.customer = Customer.objects.create(user=cls.user)

        cls.order1 = Order.objects.create(
            customer=cls.customer,
            ship_street='123 Street',
            ship_city='ACity',
            ship_postcode='AB123CD',
            date=timezone.now().date(),
            status='Open',
            uuid='123456',
            order_amount=29.99,
            ship_name='Test Customer',
            ship_phone='0123456789'
        )

        cls.orderItem1 = OrderItem.objects.create(
            order=cls.order1,
            item=cls.product2,
            quantity=1,
            price=29.99
        )

    # Test to check the store front view works and loads the books
    def test_view_storefront(self):
        response = self.client.get(reverse('store:storefront'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)
        self.assertContains(response, self.product3.name)

    # Test to check the detail page about a book 
    def test_view_book_details(self):
        # Get the detail view for book 1
        response = self.client.get(reverse('store:product-detail',
                                           args=[self.product1.id]))
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product1.author)

    # Test the registration page successfully registers a new user
    def test_user_registration(self):
        data = {
            'email': 'testuser@me.co.uk',
            'name': 'Test User',
            'password1': 'P4ssword1!',
            'password2': 'P4ssword1!',
        }
        response = self.client.post(reverse('store:signup'), data)
        # Check for successful redirect after registration
        self.assertEqual(response.status_code, 302)
        new_user = User.objects.get(email='testuser@me.co.uk')
        self.assertTrue(new_user is not None)
        self.assertTrue(Customer.objects.filter(user=new_user).exists())

    # Check an unautorised cannot access accounts page
    def test_unauthorised_user_accounts_page(self):
        response = self.client.get(reverse('store:account_page'), follow=True)
        # Check user is diverted to the login page
        self.assertRedirects(response,
                             f'/login/?next={reverse("store:account_page")}',
                             status_code=302, target_status_code=200)

    # Test that an authorised user can login and view their accounts page
    def test_authorised_user_accounts_page(self):
        # Log user in
        self.client.login(username='test@user.co.uk',
                          password='12345')
        response = self.client.get(reverse("store:account_page"))
        self.assertEqual(response.status_code, 200)
        # Confirm accounts page is loaded
        self.assertContains(response, "Your Account")
        self.assertContains(response, "Past Orders")
        self.assertContains(response, "Change Password")

    # Test the order detail view
    def test_view_order_details(self):
        # Log user in
        self.client.login(username='test@user.co.uk',
                          password='12345')
        # Get the order details for order 1
        response = self.client.get(reverse("store:order-detail",
                                           args=[self.order1.id]))
        self.assertEqual(response.status_code, 200)
        # Confirm correct order is loaded
        self.assertContains(response, self.orderItem1.item.name)
        self.assertContains(response, f'Order Number: {self.order1.id}')
        self.assertContains(response, self.order1.order_amount)
