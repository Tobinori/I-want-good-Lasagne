from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, DishViewSet, IngredientViewSet, DishIngredientViewSet, OrderViewSet, OrderItemViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'dish-ingredients', DishIngredientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
