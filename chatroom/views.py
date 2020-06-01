from django.shortcuts import render,redirect
from signup.models import Signup as sp
from .models import Chats as cht
# Create your views here.
def chat_view(request):
    try:
        text_content = request.POST["textcontn"]
        opponent_id = request.POST["opponent_id"]
        cht.objects.create(current_user_info = sp.objects.get(uid= request.session["uid"]) ,
         opponent_info_id = opponent_id , chat_content = text_content)
        return redirect("/")
    except Exception as e:
        print(e)
        return redirect("/")
