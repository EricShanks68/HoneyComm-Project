console.log("hello?");

//might want this scope var to display in cart html ? or send to varable in cart js?

function addToCart(product){
    cart.push(product);
    console.log(cart);
    let numOfItems = cart.length;
    document.getElementById("cart_balance").innerHTML = "Cart(" + numOfItems + ")";
}