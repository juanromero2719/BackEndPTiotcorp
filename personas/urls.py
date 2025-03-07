from rest_framework import routers
from django.urls import path, include
from .api import PersonaViewSet

router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet, basename='personas')

urlpatterns = [
    path('', include(router.urls)),
]
