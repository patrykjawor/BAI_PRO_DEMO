from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(UserProfile)

"""
Konfiguracja panelu administracyjnego.

Rejestruje modele `Comment` i `UserProfile` w panelu administracyjnym Django.
"""
