from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summery(request):
    return render(request, 'cart_summery.html',  {})


def cart_add(request):

    #get the cart
    cart= Cart(request)

    #test for post
    if request.POST.get('action') =='post':
        product_id = str(request.POST.get('product_id'))

        #lookup the product
        product = get_object_or_404(Product, id=product_id)

        #save the session
        cart.add(product= product)

        response = JsonResponse({'Product Name': product.name})
        return response
  

def cart_delete(request):
    pass


def cart_update(request):
    pass
