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
    def __str__(self):
        return self.first_name + " " + self.last_name

    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Kierowca"
        verbose_name_plural = "Kierowcy"


class MealCategories(models.Model):
    def __str__(self):
        return self.category_name

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, unique=True)
    category_price = models.DecimalField(max_digits=4, decimal_places=2)
    the_term_of_validity_days = models.IntegerField(choices=DAYS)

    class Meta:
        verbose_name = "Kategoria Posiłku"
        verbose_name_plural = "Kategorie Posiłków"


class Meal(models.Model):
    def __str__(self):
        return self.meal_name

    meal_name = models.CharField(max_length=50, unique=True, primary_key=True)
    meal_category = models.ForeignKey(MealCategories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Posiłek"
        verbose_name_plural = "Posiłki"


class Delivery(models.Model):
    def __str__(self):
        return self.delivery_ID

    delivery_ID = models.CharField(unique=True, primary_key=True, max_length=20)
    delivery_date = models.DateField(default=datetime.date.today(), null=False)
    meal_name = models.ManyToManyField(Meal, through="Warehouse")
    class Meta:
        verbose_name = "Dostawa"
        verbose_name_plural = "Dostawy"


class Warehouse(models.Model):
    def save(self, *args, **kwargs):
        self.the_term_of_validity = self.delivery_ID.delivery_date + datetime.timedelta(days=self.meal_name.meal_category.the_term_of_validity_days)
        super(Warehouse, self).save(*args, **kwargs)

    delivery_ID = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    meal_name = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    the_term_of_validity = models.DateField(default=datetime.date.today())

    class Meta:
        verbose_name = "Magazyn"
        verbose_name_plural = "Magazyn"
        unique_together = ['delivery_ID', 'meal_name']
