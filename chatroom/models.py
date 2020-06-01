from django.db import models
from signup.models import Signup as sp
# Create your models here.

class Chats(models.Model):
    chat_uid = models.AutoField(primary_key = True , serialize = True)
    current_user_info = models.ForeignKey(sp , on_delete = models.CASCADE , related_name = "current_user_bridge")
    opponent_info = models.ForeignKey(sp , on_delete = models.CASCADE , related_name = "opponent_user_bridge")
    chat_content = models.CharField(max_length = 1024)
    chat_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "Chats"
