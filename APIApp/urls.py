
from django.urls import path
from APIApp.views import AllProduct, SpecificProductDetail

urlpatterns = [
    path('products/', AllProduct.as_view(), name='products'),
    path('products/<int:pk>/', SpecificProductDetail.as_view(),
         name='product detail'),
]
