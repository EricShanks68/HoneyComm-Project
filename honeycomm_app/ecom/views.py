import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Product, Cart
from django.conf import settings

# Create your views here.



def products(request):
    request.session['cart_man']#initalize cart session
    myproducts = Product.objects.all().values()
    template = loader.get_template('all_products.html')
    context = {
        'myproducts': myproducts,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myproduct = Product.objects.filter(id=id)
    template = loader.get_template('details.html')
    context ={
        'myproduct': myproduct,
    }
    return HttpResponse(template.render(context, request))

def cart(request):
    mycart = None
    if request.session['cart']:
        mycart = request.session['cart']
        mycart = Product.objects.filter(id__in=mycart)
        print(mycart)
    else:
        request.session['cart'] #initalize cart session
    template = loader.get_template('cart.html')
    context ={
        'mycart': mycart,
    }
    return HttpResponse(template.render(context, request))

def add_to_cart(request):
    print(request.body.decode("utf-8"))
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    content = body["product_id"]
    content = content.replace('"', "")
    product_id = int(content)
    saved_item = request.session['cart']
    saved_item.append(product_id)
    request.session['cart'] = saved_item
    request.session['cart'].append(product_id)
    return JsonResponse({'text': 'Added item id to the cart session :)'})

def remove_from_cart(request):
    print(request.body.decode("utf-8"))
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    content = body["product_id"]
    content = content.replace('"', "")
    product_id = int(content)
    print(product_id)
    remove_item =  request.session['cart']
    remove_item.remove(product_id)
    request.session['cart'] = remove_item
    #for some reason need to remove item twice?
    remove_item =  request.session['cart']
    remove_item.remove(product_id)
    request.session['cart'] = remove_item
    return JsonResponse({'text': 'removed item id from the session :)'})
    

def main(request):
    request.session['cart_man']#initalize cart session #initalize cart session
    template = loader.get_template('main.html')
    return HttpResponse(template.render())