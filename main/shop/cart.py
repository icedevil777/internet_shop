from decimal import Decimal
from typing import Literal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request) -> None:
        """ Init cart """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """Add or update product in cart"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'slug': product.slug, 'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self) -> None:
        """Save cart in session"""
        self.session.modified = True

    def remove(self, product) -> None | Literal[True]:
        """ Delete one product from cart """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            return True

    def clear(self) -> None:
        """ Delete all products from cart """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __len__(self) -> int:
        """Count all products in cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self) -> int:
        """Calc products price in cart"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
