from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers
from .views import PerevalViewSet

router = routers.DefaultRouter()
router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('submitData/', include(router.urls)),
    path('', lambda request: redirect('/submitData/pereval', permanent=False))
]
