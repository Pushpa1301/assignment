from django.db import models

class Post(models.Model):
    first_name= models.CharField(max_length=300, unique=True)
    last_name=models.CharField(max_length=300, unique=True)
    phone_number=models.CharField(max_length=300, unique=True)
    email=models.EmailField(max_length=300, unique=True)

    content= models.TextField()












