from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RatRoom(models.Model):
    rat = models.ImageField(upload_to='static/img', default='static/img/ratonEscondido.jpg')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name 

class RatMessages(models.Model):
    room = models.ForeignKey(RatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.room) + ' ' + str(self.date_added)
    
    class Meta:
        ordering = ('date_added',)

    
class RatSticker(models.Model):
    rat = models.ImageField(upload_to='static/img/sticker')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 