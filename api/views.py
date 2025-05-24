from datetime import datetime

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from api.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


# Create your views here.
class RevenueViewSet(ViewSet):
    def list(self, request):
        try:
            start_date_filter = request.GET.get('start_date')
            end_date_filter = request.GET.get('end_date')
        except:
            return Response("invalid query param", status=400)

        product_filter = request.GET.get('product_id', None)
        category_filter = request.GET.get('category', None)
        region_filter = request.GET.get('region', None)
        start_date_obj = datetime.strptime(start_date_filter, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date_filter, "%Y-%m-%d")
        sales = Order.objects.filter(date_of_sales__range=(start_date_obj, end_date_obj))
        if product_filter:
            sales = sales.filter(product__ref=product_filter)
        if category_filter:
            sales = sales.filter(product__category=category_filter)
        if region_filter:
            sales = sales.filter(region_of_sales=region_filter)
        total_rev = self.get_total_revenue(sales)
        return Response({'total_revenue': total_rev}, status=HTTP_200_OK)

    def get_total_revenue(self, sales):
        total_revenue = 0

        for sale in sales:
            discount = sale.product.discount
            discount_amount = sale.product.unit_price * discount
            total_revenue += (sale.product.quantity * sale.product.unit_price) - discount_amount + sale.product.shipping_cost
        return total_revenue

