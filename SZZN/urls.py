"""SZZN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from systemAPP import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/login/', v.Index.as_view(), name='index'),
    path('', v.LandingPage.as_view(), name='login'),
    path('index/logout/', v.UserLogout.as_view(), name='logout'),
    path('driver/list', v.DriverList.as_view(), name='driverlist'),
    path('menu', v.MenuList.as_view(), name='menu'),
    path('warehouse/now', v.WarehouseList.as_view(), name="warehouseList")
]
