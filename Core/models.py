from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.


class ToDoModel(models.Model):
    title = models.CharField(verbose_name="", max_length=200)
    contact = models.CharField(verbose_name="", max_length=200)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')