// Function to change the quantity of an item
function changeQty(itemId, itemQty) {
    newQty = document.getElementById("itemQuantity").value;
    if (newQty < 1) {
        itemQty = 1;  // Ensure that the quantity doesn't go below 1
    } else {
        itemQty = newQty;
    }
    updateBasket(itemId, itemQty);
}

// Function to increase the quantity of an item
function increaseQty(itemId, itemQty) {
    itemQty += 1;
    updateBasket(itemId, itemQty);
}

// Function to decrease the quantity of an item
function decreaseQty(itemId, itemQty) {
    if (itemQty > 1) {
        itemQty -= 1;
        updateBasket(itemId, itemQty);
    }
}

// Function to send AJAX request to update the basket
function updateBasket(itemId, itemQty) {
    $.ajax({
        url: '/basket/update_basket/',  // Get url view to trigger update
        method: 'GET',
        data: {
            item: itemId,
            qty: itemQty
        },
        success: function(response) {
            // Passback the relevant parts to update
            $('#item-total-' + itemId).text('£' + response.line_cost);  // Update line item cost
            $('#total-price').text('£' + response.total_price);  // Update total price
            $('#basket-count').text(response.basket_count + ' items');  // Update basket count

            location.reload(); // Refresh the page after success response

        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
}

// Preload images
document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.card-img-top');
    images.forEach(image => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = image.src;
        document.head.appendChild(link);
    });
});