from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Friend(models.Model):
    follower = models.ForeignKey(User,related_name= "follower", on_delete = models.CASCADE)
    following = models.ForeignKey(User,related_name= "following" ,on_delete = models.CASCADE)
    is_accepted =  models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return f"{self.follower} following {self.following}"

