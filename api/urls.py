from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ShoppingListViewSet, ProductViewSet, UserDetailByUsername, ListDetailByListname

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'shoplists', ShoppingListViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)), 
    path('user/<str:user_name>/', UserDetailByUsername.as_view(), name='user-detail-by-username'),
    path('list/<str:list_name>/', ListDetailByListname.as_view(), name='list-detail-by-listname'),
]

# http://yourdomain.com/user/john_doe/