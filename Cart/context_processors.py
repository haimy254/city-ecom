from .cart import Cart

#create context processor so cart can work in all pages 
def cart(request):
    #return the default data form the cart
    return {'cart':Cart(request)}