from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, ShoppingList, Product
from .serializers import UserSerializer, ShoppingListSerializer, ProductSerializer
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def update(self, request, *args, **kwargs):
        shopping_list = self.get_object()
        products_data = request.data.get('products', [])

        for product_id in products_data:
            try:
                product = Product.objects.get(product_id=product_id)
                shopping_list.products.add(product)  # Directly adding without checking existing
            except Product.DoesNotExist:
                return Response({'error': f'Product with id {product_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(shopping_list)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailByUsername(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'user_name'
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        user_name = kwargs.get('user_name')
        try:
            user = User.objects.get(user_name=user_name)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ListDetailByListname(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'list_name'
    queryset = ShoppingList.objects.all()

    def get(self, request, *args, **kwargs):
        list_name = kwargs.get('list_name')
        try:
            list = ShoppingList.objects.get(list_name=list_name)
            serializer = self.get_serializer(list)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except list.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)