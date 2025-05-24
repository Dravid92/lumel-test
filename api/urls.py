from rest_framework import routers

from api.views import RevenueViewSet

router = routers.DefaultRouter()


router.register(r'revenue', RevenueViewSet, basename='Revenue')
