import os

import pandas
import requests
from django.core.management import BaseCommand

from api.models import Customer, Product, Order


class Command(BaseCommand):
    # Can be used for import and update
    def handle(self, *args, **kwargs):
        print("Downloading data...")
        # Note: Assume this is the data sheet
        url = "https://docs.google.com/spreadsheets/u/1/d/16FlCbvqT15RvbIzbHKLVpV9aB0BxEE6g8eTWDX00WAM/export?format=xlsx&id=16FlCbvqT15RvbIzbHKLVpV9aB0BxEE6g8eTWDX00WAM"
        r = requests.get(url, allow_redirects=True)
        with open("lumel.xlsx", "wb") as f:
            f.write(r.content)
        df = pandas.read_excel('lumel.xlsx')
        print(df.columns)
        for index, row in df.iterrows():
            customer_exists = Customer.objects.filter(email=row['Customer Email']).exists
            if not customer_exists:
                customer, _ = Customer.objects.create(
                    name=row['Customer Name'],
                    email=row['Customer Email'],
                    address=row['Customer Address']
                )

            product_exists = Product.objects.filter(ref=row['Product ID']).exists
            if not product_exists:
                product, _ = Product.objects.create(
                    name=row['Product Name'],
                    category=row['Category'],
                    region=row['Unit Price'],
                    quantity=row['Quantity Sold'],
                    discount=row['Discount'],
                    shipping_cost=row['Shipping Cost'],
                )
            order_exists = Order.objects.filter(id=row['Order ID']).exists
            date_of_sale = str(row['Date of Sale'])
            if not order_exists:
                order, created = Order.objects.create(
                    date_of_sales=date_of_sale,
                    payment_method=row['Payment Method'],
                    region_of_sales=row['Region'],
                    customer_id=customer.id,
                    product_id=product.id
                )
        return 1
