from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from .forms import LoginUser
from .models import Driver, Menu, MenuCategories

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


class MenuList(View):
    template_name = "menu.html"
    def get(self, request):
        menu = Menu.objects.all().order_by('meal_name')
        if menu:
            category = MenuCategories.objects.all().order_by('category_name')
            context = {
                'category': category,
                'menu': menu
                }
            return render(request, self.template_name, context)

