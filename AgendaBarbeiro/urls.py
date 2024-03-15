from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from salon.views import SalonViewSet, LocationViewSet
from promotion.views import PromotionListAPIView
from schedule.views import ScheduleListAPIView
from booking.views import BookingViewSet
from service.views import ServiceViewSet, ClientServiceViewSet
from clientuser.views import ClientViewSet
from collaborator_user.views import CollaboratorViewSet, SalonCollaboratorViewSet


router = routers.DefaultRouter()
router.register("salon", SalonViewSet, basename="salon")
router.register("location", LocationViewSet, basename="location")
router.register("promotions", PromotionListAPIView, basename="promotion")
router.register("schedules", ScheduleListAPIView, basename="schedule")
router.register("service", ServiceViewSet, basename="service")
router.register("client_service", ClientServiceViewSet, basename="client_service")
router.register("client", ClientViewSet, basename="client")
router.register("collaborator", CollaboratorViewSet, basename="collaborator")
router.register(
    "salon_collaborator", SalonCollaboratorViewSet, basename="salon_collaborator"
)
router.register("create-booking", BookingViewSet, basename="create-booking"),
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    
]
