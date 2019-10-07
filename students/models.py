from django.db import models
from django.contrib.auth.models import User


class details(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=50)
    username=models.ForeignKey(User,unique=True,on_delete=models.CASCADE)
    student_dpt=models.CharField(max_length=100)
    student_img=models.ImageField(upload_to="static")
    password = models.CharField(max_length=50)
