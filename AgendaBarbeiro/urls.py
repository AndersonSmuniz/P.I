from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from salon.views import SalonViewSet, LocationViewSet

route = routers.DefaultRouter()
route.register("salon", SalonViewSet, basename="Salons")
route.register("location", LocationViewSet, basename="Locations")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(route.urls)),
]
