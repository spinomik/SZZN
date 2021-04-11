from django.db import models

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(unique=True)
    def __str__(self):
        return self.first_name + " " + self.last_name

class MenuCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, unique=True)
    category_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.category_name

class Menu(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=50, unique=True)
    meal_category = models.ForeignKey(MenuCategories, on_delete=models.CASCADE)
    def __str__(self):
        return self.meal_name



