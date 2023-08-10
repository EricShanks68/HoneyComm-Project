/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


function add_to_cart(product){
    console.log(product)
    fetch("/add_to_cart/", {
  method: "POST",
  body: JSON.stringify({
    product_id: product,
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})
  .then((response) => response.json())
  .then((json) => console.log(json));
}

function remove_from_cart(product){
    console.log(product)
    fetch("/remove_from_cart/", {
  method: "POST",
  body: JSON.stringify({
    product_id: product,
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})
  .then((response) => response.json())
  .then((json) => console.log(json));
}
