from django.db import models

# Create your models here.
class Users(models.Model):
    Users_id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=50)
    Create_time=models.DateTimeField(auto_now_add=True)
    Games=models.CharField(max_length=50)

class Games(models.Model):
    Game_id=models.AutoField(primary_key=True)
    Game_name=models.CharField(max_length=50)

class File(models.Model):
    image = models.ImageField(upload_to='game/image', default="")


