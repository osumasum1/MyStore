from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet, products_by_catergory

router = SimpleRouter(trailing_slash=False)
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('products-by-category', products_by_catergory, name='products_by_category'),
]
