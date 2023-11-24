from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from .models import UserProfile

class UserForm(UserCreationForm):
    """
    Formularz rejestracji użytkownika z możliwością włączenia uwierzytelniania dwuetapowego.

    Dziedziczy po klasie UserCreationForm i dodaje pole `email` oraz `enable_2fa` do standardowego formularza rejestracji.
    """
    email = forms.EmailField(required=True)
    enable_2fa = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Enable Two-Factor Authentication'
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        """
        Zapisuje użytkownika oraz, jeśli włączono uwierzytelnianie dwuetapowe,
        tworzy i zapisuje urządzenie TOTP dla tego użytkownika.
        
        Args:
        commit (bool): Określa, czy operacja zapisu ma zostać wykonana natychmiastowo (domyślnie True).
        
        Returns:
        User: Obiekt użytkownika, który został zapisany.
        """
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        if self.cleaned_data['enable_2fa']:
            totp_device = TOTPDevice.objects.create(user=user, confirmed=False)
            totp_device.save()
            profile = UserProfile.objects.get_or_create(user=user)
            profile.totp_device = totp_device
            profile.save()

        return user