from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, CategoryDetailView, ProductDetailView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='MyProduct')
router.register(r'categories', CategoryViewSet, basename='MyCategory')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/categories/<int:pk>', CategoryDetailView.as_view(), name="category-detail"),
    path('api/product/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]  # path('categories/<int:pk>/product/', CategoryProduct.as_view()),
