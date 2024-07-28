# ecommerce/product_management.py

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def list_products(self):
        return self.products
