from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from .views import (
    ProductDetailView,
    ProductListView,
    CategoryDetailView,
    CategoryListView,
    СartView,
    СartDetailView,
    OrderCreateView,
    OrderDetailView
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api/product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("api/category/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("api/products/", ProductListView.as_view(), name="product_list"),
    path("api/categories/", CategoryListView.as_view(), name="category_list"),
    path("api/cart/", СartView.as_view(), name="cart"),
    path("api/cart/<int:pk>", СartDetailView.as_view(), name="detail_cart"),
    path('api/cart/order/', OrderCreateView.as_view(), name='create_order'),
    path('api/cart/order/<int:pk>', OrderDetailView.as_view(), name='detail_order'),
]
