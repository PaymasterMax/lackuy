from django.conf.urls import url
from . import views
app_name = "stockmanager"

urlpatterns = [
    url("^$" , views.stockview , name  = "stocks"),
]
