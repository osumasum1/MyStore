from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import OrderViewSet

router = SimpleRouter(trailing_slash=False)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
