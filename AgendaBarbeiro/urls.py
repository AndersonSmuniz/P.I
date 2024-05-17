from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from salon.views import FavoriteViewSet, SalonViewSet, LocationViewSet
from promotion.views import PromotionListAPIView
from schedule.views import AvailableScheduleViewSet, AvailableSlotsView
from booking.views import BookingViewSet
from service.views import ServiceViewSet, CategoryServicesView, CategoryView
from clientuser.views import (
    ClientCreateViewSet,
    ClientUpdateViewSet,
    ClientDestroyViewSet,
)
from collaborator_user.views import (
    CollaboratorViewSet,
    SalonCollaboratorViewSet,
    CollaboratorSalonView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register("salon", SalonViewSet, basename="salon")
router.register("location", LocationViewSet, basename="location")
router.register("promotions", PromotionListAPIView, basename="promotion")
router.register("schedules", AvailableScheduleViewSet, basename="schedule_list")
router.register("service", ServiceViewSet, basename="service")
router.register("collaborator", CollaboratorViewSet, basename="collaborator")
router.register(
    "salon_collaborator", SalonCollaboratorViewSet, basename="salon_collaborator"
)
router.register("create-booking", BookingViewSet, basename="create-booking")
router.register("client/create", ClientCreateViewSet, basename="client-create")
router.register("client/update", ClientUpdateViewSet, basename="client-update")
router.register("client/delete", ClientDestroyViewSet, basename="client-destroy")
router.register("favorite", FavoriteViewSet, basename="favorite")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("salon/<int:id>/category", CategoryView.as_view(), name="category"),
    path(
        "category/<int:id>/services",
        CategoryServicesView.as_view(),
        name="salon_services",
    ),
    path(
        "salon/<int:id>/collaborators",
        CollaboratorSalonView.as_view(),
        name="salon_collaborators",
    ),
    path(
        "schedule/barber/<int:barber>/date/<str:date>/",
        AvailableSlotsView.as_view(),
        name="schedule_free",
    ),
    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
