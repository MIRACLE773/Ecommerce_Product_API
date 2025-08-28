from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    recipient =models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    verb = models.CharField(max_length=200)
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct', 'target_id')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.actor} {self.verb} {self.target}  {self.recipient}"