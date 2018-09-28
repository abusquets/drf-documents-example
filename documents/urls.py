from django.urls import path, include
from rest_framework import routers

from .api import DocumentViewSet


router = routers.DefaultRouter()
router.register('documents', DocumentViewSet,
                base_name='documents')

urlpatterns = [
    path('v1/', include(router.urls))]
