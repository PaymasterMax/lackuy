from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include

urlpatterns = [
    url("^$" , include("home.urls")),
    url("^login/" , include("login.urls")),
    url("^signup/$" , include("signup.urls")),
    url("^orders/" , include("orders.urls")),
    url("^stockmanager/" , include("stockmanager.urls")),
    url("^/chatroom" , include("chatroom.urls")),
    url('admin/', admin.site.urls),
]
