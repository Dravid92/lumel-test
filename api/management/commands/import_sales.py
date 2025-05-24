import os
from datetime import datetime

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
            customer = Customer.objects.filter(email=row['Customer Email'])
            if not customer:
                customer = Customer.objects.create(
                    name=row['Customer Name'],
                    email=row['Customer Email'],
                    address=row['Customer Address']
                )
            else:
                customer = customer.first()
                customer.name = row['Customer Name']
                customer.address = row['Customer Address']
                customer.save()

            product = Product.objects.filter(ref=row['Product ID'])
            if not product:
                product = Product.objects.create(
                    name=row['Product Name'],
                    category=row['Category'],
                    unit_price=row['Unit Price'],
                    quantity=row['Quantity Sold'],
                    discount=row['Discount'],
                    shipping_cost=row['Shipping Cost'],
                    ref=row['Product ID']
                )
            else:
                product = product.first()
                product.name = row['Product Name']
                product.category = row['Category']
                product.unit_price = row['Unit Price']
                product.quantity = row['Quantity Sold']
                product.discount = row['Discount']
                product.shipping_cost = row['Shipping Cost']
                product.save()
            order = Order.objects.filter(ref=row['Order ID'])
            date_of_sale = datetime.strptime(str(row['Date of Sale']), "%Y-%m-%d %H:%M:%S").date()
            if not order:
                order = Order.objects.create(
                    date_of_sales=date_of_sale,
                    payment_method=row['Payment Method'],
                    region_of_sales=row['Region'],
                    customer_id=customer.id,
                    product_id=product.id,
                    ref=row['Order ID']
                )
            else:
                order = order.first()
                order.date_of_sales = date_of_sale
                order.payment_method = row['Payment Method']
                order.region_of_sales = row['Region']
                order.customer_id = customer.id
                order.product_id = product.id
                order.save()
        return "all ok"
