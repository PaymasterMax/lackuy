from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include

urlpatterns = [
    url("^$" , include("home.urls")),
    url("^orders/" , include("orders.urls")),
    url("^stockmanager/" , include("stockmanager.urls")),
    url('admin/', admin.site.urls),
]
