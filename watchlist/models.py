from django.db import models

# Create your models here.
class script(models.Model):
    code = models.CharField(max_length = 16)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    buy_quantity = models.IntegerField(default=0)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    sell_quantity = models.IntegerField(default=0)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    change = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    change_percentage = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    state = models.CharField(max_length = 2,default='un')


