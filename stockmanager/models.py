from django.db import models
from signup.models import Signup as sp
# Create your models here.

class Stock(models.Model):
    stock_id = models.AutoField(primary_key = True , serialize = True , unique = True)
    stock_poster = models.ForeignKey(sp , on_delete = models.CASCADE)
    stock_name = models.CharField(max_length = 50)
    stock_description = models.CharField(max_length = 255)
    stock_price = models.IntegerField(max_length = 6)
    stock_post_date = models.DateTimeField(auto_now_add = True)
