from django.db import models
from django.contrib.auth.models import User

DIET_CHOICES = [
    ('vegan', 'Vegan'),
    ('vegetarian', 'Vegetarian'),
    ('gluten_free', 'Gluten-Free'),
    ('omnivore', 'Omnivore'),
    ('lactose_free', 'Lactose-Free'),
    ('low_carb', 'Low Carb'),
    ('low_fat', 'Low Fat'),
    ('high_protein', 'High Protein'),
    # TODO Check is there any other options, user should be able to add multiple choices
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    surname = models.CharField(max_length=255, blank=True)
    diet = models.CharField(max_length=255, blank=True)
    allergy = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


# 🏢 Restaurant Model
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    seatings = models.PositiveIntegerField()


    def __str__(self):
        return self.name

# 🍽️ Dish Model
class Dish(models.Model):
    name_en = models.CharField(max_length=255)  # English Name
    name_de = models.CharField(max_length=255, blank=True, null=True)  # German Name (for multi-language)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='dishes/', blank=True, null=True)
    def get_allergy_info(self):
        return list(set(ingredient.allergy_info for ingredient in self.ingredients.all() if ingredient.allergy_info))

    def get_diet_info(self):
        return list(set(ingredient.diet_info for ingredient in self.ingredients.all() if ingredient.diet_info))

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name_en

# 🥦 Ingredient Model
class Ingredient(models.Model):
    name_en = models.CharField(max_length=255)
    name_de = models.CharField(max_length=255, blank=True, null=True)
    calories = models.IntegerField(null=True, blank=True)
    allergy_info = models.JSONField(blank=True, null=True)  # JSONField for multiple allergies
    diet_info = models.JSONField(blank=True, null=True)     # JSONField for multiple diets
    origin = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name_en

# 🔗 Dish-Ingredient Relationship
class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(help_text="Amount in grams or ml", null = True, blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    class Meta:
        unique_together = ('dish', 'ingredient')



# 🛒 Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

# 🍲 Order Items
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

# ⭐ Review Model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # e.g., 1-5 stars
    comment = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'dish')
