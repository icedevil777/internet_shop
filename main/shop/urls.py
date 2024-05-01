from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from .views import (
    ProductViewSet,
    CategoryViewSet,
    CategoryDetailView,
    ProductDetail,
    ProductList,
)

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="MyProduct")
router.register(r"categories", CategoryViewSet, basename="MyCategory")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include(router.urls)),
    path("api/v1/categories/<int:pk>", CategoryDetailView.as_view(), name="category-detail",),
    path("api/v2/product/<int:pk>", ProductDetail.as_view(), name="product-detail"),
    path("api/v2/products/", ProductList.as_view(), name="product_list"),
    # Spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
]
