from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:

    def __init__(self, request):
        """ Init cart """
        self.session = request.session
        print('self.session', self.session)
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """Add or update product in cart"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Save cart in session"""
        self.session.modified = True

    def remove(self, product):
        """ Delete product from cart """

    def __iter__(self):
        """Get products from db"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all products in cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Calc products price in cart"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
