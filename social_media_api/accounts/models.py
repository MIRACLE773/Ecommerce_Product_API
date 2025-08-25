from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=200, blank=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='profile_pics/')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follower_users', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)

    email = models.EmailField(unique=True)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    
    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
