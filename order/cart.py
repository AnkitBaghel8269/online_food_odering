from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from restaurant.models import OurMenu

class Cart(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.food_name,
                'quantity': 1,
                'price': str(product.food_price)
                
                
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.food_name,
                    'quantity': 1,
                    'price': str(product.food_price),
                }

        self.save()
    # def __iter__(self):
    #     product_ids = self.cart.keys()
    #     products = OurMenu.objects.filter(id__in=product_ids)
    #     cart = self.cart.copy()


    #     for product in products:
    #         cart[str(product.id)]['product'] = product
        
    #     for item in cart.values():
    #         item['food_price'] = Decimal(item['food_price'])
    #         item['total_price'] = item['food_price'] * item['qty']
    #         item['total_charge'] = 10 * item['qty']
    #         item['all_total_price'] +=  item['total_price'] 
    #         yield item

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('food_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True




