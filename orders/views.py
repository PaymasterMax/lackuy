from django.shortcuts import render

# Create your views here.

def ordersview(request):
    return render(request , "orders/orders.html")
