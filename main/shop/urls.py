from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import ProductDetailView, ProductListView, CategoryDetailView, CategoryListView


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("api/category/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("api/products/", ProductListView.as_view(), name="product_list"),
    path("api/categories/", CategoryListView.as_view(), name="category_list"),
]


