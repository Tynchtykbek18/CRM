from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DealView


router = DefaultRouter()
router.register('deals', DealView)


urlpatterns = [
    path('', include(router.urls)),
]

