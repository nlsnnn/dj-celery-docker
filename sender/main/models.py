from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')