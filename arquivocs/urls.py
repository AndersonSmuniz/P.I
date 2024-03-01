from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'schedules', views.ScheduleListAPIView)
router.register(r'promotions', views.PromotionListAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('schedules/<int:pk>/', views.ScheduleDetailAPIView.as_view()),
    path('promotions/<int:pk>/', views.PromotionDetailAPIView.as_view()),
]
