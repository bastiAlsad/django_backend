from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import random
import string
# Create your models here.

def randomLoginCode():
    code = 'LX-'
    for i in range(4):
        number = random.randint(0,9)
        code += str(number)
    return code

def random_string(length=100):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string



    
class Laxout_Exercise(models.Model):
    execution = models.CharField(max_length=400,default="")
    name = models.CharField(max_length=40,default="")
    dauer = models.IntegerField(default=30)
    videoPath = models.CharField(max_length=100,default="")
    looping = models.BooleanField(default=False)
    added = models.BooleanField(default=False)
    instruction = models.CharField(max_length=200, default="")
    timer = models.BooleanField(default=False)
    required = models.CharField(max_length=50, default="")
    imagePath = models.CharField(max_length=50, default="")

class Laxout_User(models.Model):
    laxout_user_name = models.CharField(max_length=200, default="")
    user_uid = models.CharField(max_length=80, default= random_string())
    access_code = models.CharField(max_length=1000, default= randomLoginCode(), blank=True, null=True)
    laxout_credits = models.IntegerField(default=0)
    creation_date = models.DateField(default= timezone.now())
    exercises = models.ManyToManyField(Laxout_Exercise)
    note = models.CharField(max_length=200, default="")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)










