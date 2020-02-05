from django.db import models


class House(models.Model):
    address = models.CharField(max_length=120)
    year = models.IntegerField(default=1)
class  Brick(models.Model):
    num = models.IntegerField(default=0)
    house = models.OneToOneField(House,on_delete = models.CASCADE,related_name="hous")
