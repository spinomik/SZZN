from django.db import models
import datetime
DAYS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
)

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
    the_term_of_validity_days = models.IntegerField(choices=DAYS)
    def __str__(self):
        return self.category_name

class Menu(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=50, unique=True)
    meal_category = models.ForeignKey(MenuCategories, on_delete=models.CASCADE)
    def __str__(self):
        return self.meal_name

class Warehouse(models.Model):
    delivery_ID = models.AutoField
    meal_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    delivery_date = models.DateField(default=datetime.date.today(), null=False)
    the_term_of_validity = models.DateField(default=datetime.date.today())

    def save(self, *args, **kwargs):
        self.the_term_of_validity = self.delivery_date + datetime.timedelta(days=self.meal_name.meal_category.the_term_of_validity_days)
        super(Warehouse, self).save(*args, **kwargs)


