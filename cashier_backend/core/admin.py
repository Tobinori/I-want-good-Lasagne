from django.contrib import admin
from .models import Restaurant, Dish, Ingredient, Order, OrderItem, Review, DishIngredient

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(DishIngredient)
