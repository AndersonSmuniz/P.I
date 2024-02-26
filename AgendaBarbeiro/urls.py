from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from salon.views import SalonViewSet, LocationViewSet
from promotion.views import PromotionListAPIView
from schedule.views import ScheduleListAPIView

route = routers.DefaultRouter()
route.register("salon", SalonViewSet, basename="Salons")
route.register("location", LocationViewSet, basename="Locations")
route.register("schedules", ScheduleListAPIView, basename="Schedule")
route.register("promotions", PromotionListAPIView, basename="Promotion") 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(route.urls)),
]
