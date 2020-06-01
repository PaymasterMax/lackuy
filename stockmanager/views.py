from django.shortcuts import render

# Create your views here.

def stockview(request):
    return render(request , "stocks/stocks.html")
