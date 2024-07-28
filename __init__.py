# ecommerce/__init__.py

from .product_management import ProductManager
from .order_processing import OrderProcessor

__all__ = ['ProductManager', 'OrderProcessor']
