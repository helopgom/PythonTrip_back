from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreferenceViewSet

router = DefaultRouter()
router.register(r'preferences', PreferenceViewSet, basename='preferences')

urlpatterns = [
    path('', include(router.urls)),
]