from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from .forms import LoginUser, DeliveryForm
from .models import Driver, Meal, MealCategories, Warehouse, Delivery

from datetime import date


today = date.today()
user = get_user_model()
class Index(View):
    def get(self, request):
        return render(request, "index.html")
    def post(self, request):
        return render(request, "index.html")

class LandingPage(FormView):
    form_class = LoginUser
    template_name = 'login.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        username = form.cleaned_data['login']
        userpaswd = form.cleaned_data['password']
        user = authenticate(username=username, password=userpaswd)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class UserLogout(RedirectView):
    url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class DriverList(View):
    template_name = "driverlist.html"
    def get(self, request):
        drivers = Driver.objects.all().order_by('last_name')
        if drivers:
            context = {
                'drivers': drivers
            }
            return render(request, self.template_name, context)
        else:
            messages.add_message(request, messages.INFO, 'Brak kierowcow do wyswietlenia')
            return render(request, "index.html")


class MenuList(View):
    template_name = "menu.html"
    def get(self, request):
        menu = Meal.objects.all().order_by('meal_name')
        if menu:
            category = MealCategories.objects.all().order_by('category_name')
            context = {
                'category': category,
                'menu': menu
                }
            return render(request, self.template_name, context)
        else:
            messages.add_message(request, messages.INFO, 'Brak produktow do wyswietlenia')
            return render(request, "index.html")


class WarehouseList(View):
    template_name = "warehouse.html"
    def get(self, request):
        warehouse = Warehouse.objects.all().order_by("quantity")
        today = date.today()

        if warehouse:
            category = MealCategories.objects.all().order_by('category_name')
            context = {
                'today': today,
                'category': category,
                'warehouse': warehouse
            }
            print(today)
            return render(request, self.template_name, context)
        else:
            messages.add_message(request, messages.INFO, 'Brak produktow do wyswietlenia')
            return render(request, "index.html")

class DeliveryAdd(View):
    template_name = "delivery.html"
    form_class = DeliveryForm
    def get(self, request):
        menu = Meal.objects.all().order_by('meal_name')
        last_delivery_id = Warehouse.objects.latest('delivery_ID')
        last_delivery_id = last_delivery_id.delivery_ID
        if menu:
            category = MealCategories.objects.all().order_by('category_name')
            context = {
                'today': today,
                'category': category,
                'menu': menu,
                'last_delivery_id': last_delivery_id
            }
            return render(request, self.template_name, context)
        else:
            messages.add_message(request, messages.INFO, 'Brak produktow do wyswietlenia')
            return render(request, "index.html")
    def post(self, request):
        deivery_id = request.POST.get('delivery_ID')
        deivery_date = request.POST.get('delivery_date')
        if deivery_id != None and deivery_date != None:
            try:
                Delivery.objects.create(delivery_ID=deivery_id, delivery_date=deivery_date)
            except IntegrityError:
                messages.add_message(request, messages.INFO, 'Podany numer zamówienia już istnieje!')
                return render(request, "index.html")
            except ValidationError:
                messages.add_message(request, messages.INFO, 'Nieprawidłowa Data!')
                return render(request, "index.html")
        for key, value in request.POST.items():
            if (key == "csrfmiddlewaretoken" or key == "delivery_date" or key =="delivery_ID" or key == "submit"):
                pass
            else:
                if(key == value):
                    meal_name= key
                else:
                    meal_qantity = value
                    Warehouse.objects.create(
                    delivery_ID=Delivery.objects.get(delivery_ID=deivery_id), meal_name=Meal.objects.get(meal_name=meal_name), quantity=meal_qantity
                )
                messages.add_message(request, messages.INFO, 'Dodano Zamówienie do bazy danych')
        return render(request, "index.html")