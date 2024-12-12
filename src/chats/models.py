from django.db import models
from friends.models import Friend
from django.contrib.auth.models import User
# Create your models here.


class ChatRoom(models.Model):
    sender = models.ForeignKey(User,related_name= "sender", on_delete = models.CASCADE)
    receiver = models.ForeignKey(User,related_name= "receiver", on_delete = models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    unread_messages = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.sender.username} send to {self.receiver.username}"
        
    
    
    
    