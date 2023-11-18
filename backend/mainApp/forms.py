from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from .models import UserProfile

class UserForm(UserCreationForm):
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