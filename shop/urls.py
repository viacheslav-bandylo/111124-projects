from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.serializers import ProductDetailCreateUpdateSerializer
from shop.views import CategoryViewSet, SupplierViewSet, ProductListCreateView, ProductRetrieveUpdateDestroyView, \
    ProductDetailViewSet, AddressViewSet, CustomerViewSet, OrderViewSet

# Создаем экземпляр роутера
router = DefaultRouter()

# Регистрируем наш ViewSet.
# 'category' - это префикс URL, по которому будут доступны наши категории.
# CategoryViewSet - представление, которое будет обрабатывать запросы.
router.register('category', CategoryViewSet)
router.register('supplier', SupplierViewSet)
router.register('product-detail', ProductDetailViewSet)
router.register('address', AddressViewSet)
router.register('customer', CustomerViewSet)
router.register('order', OrderViewSet)

# Основной список маршрутов нашего приложения.
# Мы просто включаем в него все URL, которые сгенерировал роутер.
urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
