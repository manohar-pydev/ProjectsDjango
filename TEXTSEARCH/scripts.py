from django.db.models import Subquery,OuterRef
from home.models import Product
import requests


url = "https://dummyjson.com/products?linit=300"
response = requests.get(url)
data = response.json()

for product_data in data['products']:
    try:
        product = Product(
            title = product_data['title'],
            description = product_data['description'],
            category = product_data['category'],
            price = product_data['price'],
            brand = product_data['brand'],
            sku = product_data['sku'],
            thumbnail = product_data['thumbnail']
        )
        product.save()
    except Exception as e:
        print(e)