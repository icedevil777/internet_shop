from django.urls import include, path
from rest_framework import routers

from views import ProductViewSet, CategorySerializer

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategorySerializer)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
