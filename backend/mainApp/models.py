from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

class Comment(models.Model):
    """
    Model reprezentujący komentarze.

    Atrybuty:
    - title (str): Tytuł komentarza.
    - comment (str): Treść komentarza.
    - date_time (datetime): Data i czas utworzenia komentarza (domyślnie aktualna data i czas).
    """
    title = models.CharField(max_length=128)
    comment = models.TextField()
    date_time = models.DateTimeField(default=now)


class UserProfile(models.Model):
    """
    Model reprezentujący profil użytkownika.

    Atrybuty:
    - user (User): Odwołanie do modelu użytkownika (User).
    - totp_device (TOTPDevice): Odwołanie do modelu TOTPDevice (uwierzytelnianie dwuetapowe).
    - enable_2fa (bool): Flaga określająca, czy użytkownik włączył uwierzytelnianie dwuetapowe.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totp_device = models.OneToOneField(TOTPDevice, null=True, blank=True, on_delete=models.CASCADE)
    enable_2fa = models.BooleanField(default=False)
    
    def __str__(self):
        """
        Zwraca czytelny opis profilu użytkownika.
        """
        return f"UserProfile for {self.user.username}"
