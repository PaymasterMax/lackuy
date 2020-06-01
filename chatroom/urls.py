from django.conf.urls import url
from . import views
app_name = "chatroom"

urlpatterns = [
    url("^$" , views.chat_view , name = "chat_view")
]
