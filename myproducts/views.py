from rest_framework import viewsets
from .models import Products, Categories
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
def products_by_catergory(request):
    data = []
    
    try:
        for category in Categories.objects.all():
            products = Products.objects.filter(category_id = category)
            products_data = ProductSerializer(products,many=True).data
            data.append({
                category.name: products_data
            })
        return Response(data, status=200)
    except:
        return Response(data, status=200)