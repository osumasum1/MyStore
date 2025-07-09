from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ClientViewSet

router = SimpleRouter(trailing_slash=False)
router.register('clients', ClientViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
