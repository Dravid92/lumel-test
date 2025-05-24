import os
from datetime import datetime

import pandas
import requests
from django.core.management import BaseCommand

from api.models import Customer, Product, Order
from lumel.settings import BASE_DIR


class Command(BaseCommand):
    # Can be used for import and update
    def handle(self, *args, **kwargs):
        print("Downloading data...")
        url = "https://docs.google.com/spreadsheets/u/1/d/16FlCbvqT15RvbIzbHKLVpV9aB0BxEE6g8eTWDX00WAM/export?format=xlsx&id=16FlCbvqT15RvbIzbHKLVpV9aB0BxEE6g8eTWDX00WAM"
        r = requests.get(url, allow_redirects=True)
        with open("lumel.xlsx", "wb") as f:
            f.write(r.content)
        df = pandas.read_excel('lumel.xlsx')
        print(df.columns)
        for index, row in df.iterrows():
            customer, _ = Customer.objects.get_or_create(
                id=row['Customer ID'],


            )

            product, _ = Product.objects.get_or_create(
                id=row['Product ID'],
            )
            date_of_sale = str(row['Date of Sale'])
            order, created = Order.objects.update_or_create(
                id=row['Order ID'],
            )