from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=128)
    comment = models.TextField()
    date_time = models.DateTimeField(default=now)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totp_device = models.OneToOneField(TOTPDevice, null=True, blank=True, on_delete=models.CASCADE)
    enable_2fa = models.BooleanField(default=False)
    
    def __str__(self):
        return f"UserProfile for {self.user.username}"
