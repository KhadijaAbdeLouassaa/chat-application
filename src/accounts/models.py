from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    thumbnail = models.ImageField(upload_to="images",  default="default_thumbnail.png")
    is_active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.thumbnail:
            img = Image.open(self.thumbnail.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.thumbnail.path)
                
    
    def get_online_status(self):
        if self.is_active :
            return True
        else :
            return False
    
    def __str__(self):
        return self.user.username
        
 
def create_profile(sender, **kwargs):
	if kwargs['created']:
		Profile.objects.get_or_create(user=kwargs['instance'])
        
post_save.connect(create_profile,User)
