# ecommerce/order_processing.py

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def total_amount(self):
        return self.product.price * self.quantity

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def create_order(self, order_id, product, quantity):
        order = Order(order_id, product, quantity)
        self.orders.append(order)
        return order

    def list_orders(self):
        return self.orders
