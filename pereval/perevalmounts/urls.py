from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers
from .views import PerevalViewSet

router = routers.DefaultRouter()
router.register(r'SubmitData', PerevalViewSet, basename='SubmitData')

urlpatterns = [
    path('pereval/', include(router.urls)),
    path('', lambda request: redirect('pereval/SubmitData/', permanent=False))
]
