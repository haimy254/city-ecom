

class Cart():
    def __init__(self,request):
        self.session = request.session

        #get the currrent key of  the session
        cart = self.session.get('session_key')

        #if the user is new, no session key, we create one 
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is available in all the pages of the site
        self.cart = cart