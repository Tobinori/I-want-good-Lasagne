from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from .models import Restaurant, Dish, Ingredient, DishIngredient, Order, OrderItem, Review

from .serializers import RestaurantSerializer, DishSerializer, IngredientSerializer, DishIngredientSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer


# 🍽️ Restaurant API
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# 🍕 Dish API
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

# 🥦 Ingredient API
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

# 🔗 Dish-Ingredient API
class DishIngredientViewSet(viewsets.ModelViewSet):
    queryset = DishIngredient.objects.all()
    serializer_class = DishIngredientSerializer

# 🛒 Order API
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# 🍲 OrderItem API
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# ⭐ Review API
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
