function changeQty(itemId, itemQty) {
    if (itemQty < 1) {
        window.location.href = "basket/";
    } else {
        window.location.href = "update_basket/?item=" + itemId + "&qty=" + itemQty;
    }
}


// increase quantity of item in basket
function increaseQty(itemId, itemQty) {
    itemQty += 1;
    window.location.href = "update_basket/?item=" + itemId + "&qty=" + itemQty;
}

// decrease quantity of item in basket
function decreaseQty(itemId, itemQty) {
    itemQty += -1;
    window.location.href = "update_basket/?item=" + itemId + "&qty=" + itemQty;

}
