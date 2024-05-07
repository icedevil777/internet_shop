from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import CategorySerializer
from .models import Product, Category
from django.urls import include, path, reverse


class ProductTestCase(APITestCase):

    def test_empty_product_list(self) -> None:
        url: str = reverse('product-list')
        response: HttpResponse = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.count(), 0)

    def test_empty_category_list(self) -> None:
        url: str = reverse('category-list')
        response: HttpResponse = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Category.objects.count(), 0)

    # def test_create_category(self) -> None:
    #     url: str = reverse('category_list')
    #     data: dict[str, str] = {"name": "Fruits", "slug": "fruits"}
    #     response: HttpResponse = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Category.objects.count(), 1)

    # def test_wrong_create_category(self) -> None:
    #     url: str = reverse('category_list')
    #     data: dict[str, str] = {"slug": "slug"}
    #     response: HttpResponse = self.client.post(url, data, format='json')
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, 400)

    # def test_category_detail(self) -> None:
    #     response: HttpResponse = self.client.get('/api/category/1', format='json')
    #     print(response.data)
        # self.assertEqual(response.status_code, 200)

    # def test_create_product(self) -> None:
    #     url: str = reverse('product_create')
    #     data: dict[str, str] = {"name": "Mango", "slug": "mango", "price": 100, "Available": True, "category": 0}
    #     response: HttpResponse = self.client.post(url, data, format='json')
    #     print(response.data, 'response.data')
        # self.assertEqual(response.status_code, 400)
        # self.assertEqual(Category.objects.count(), 1)


class CategorySerializerTestCase(TestCase):

    def test_ok(self) -> None:
        cat_1 = Category.objects.create(name='Fruits', slug='fruits')
        cat_2 = Category.objects.create(name='Alcohol', slug='alcohol')
        data = CategorySerializer([cat_1, cat_2], many=True, context={'request': None}).data
        expected_data = [
            {
                'url': '/api/category/1',
                'products': [],
                'name': "Fruits",
                'slug': "fruits"
            },
            {
                'url': '/api/category/2',
                'products': [],
                'name': "Alcohol",
                'slug': "alcohol"
            }
        ]
        self.assertEqual(expected_data, data)
