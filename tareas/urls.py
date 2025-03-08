from rest_framework import routers
from django.urls import path, include
from .api import TareaViewSet

router = routers.DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tareas')

urlpatterns = [
    path('', include(router.urls)),
]