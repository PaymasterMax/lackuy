from django.shortcuts import render
from signup.models import Signup as sp
from stockmanager.models import Stock as st
from chatroom.models import Chats as cht
from django.db.models import Q
# Create your views here.

def homeview(request):
    try:
        current_user = sp.objects.get(uid = request.session["uid"])
    except Exception as e:
        print(e)
        return render(request , "home/home.html")
    else:
        chats = cht.objects.filter(Q(current_user_info_id = current_user.uid)|Q(opponent_info = current_user.uid))
        all_stock = st.objects.all()
        return render(request , "home/home.html" , context = {"user_info":current_user , "all_stock":all_stock , "chats":chats})
