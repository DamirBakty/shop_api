from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ListProducts, GetProduct, ListCategories, GetCategory, CategoryProducts

app_name = 'api'

urlpatterns = [
    path('products/', ListProducts.as_view()),
    path('categories/', ListCategories.as_view()),
    path('products/<int:pk>', GetProduct.as_view()),
    path('categories/<int:pk>', GetCategory.as_view()),
    path('categories/<int:id>/products/', CategoryProducts.as_view()),
]
