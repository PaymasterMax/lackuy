from django.shortcuts import render

# Create your views here.

def stockview(request):
    return render(request , "stockmanager/stocks.html")
