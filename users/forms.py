from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible


# Methods for checking valid Uni Sydney email
@deconstructible
class WhitelistEmailValidator(EmailValidator):

    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


# Users only allowed to register using uni emails
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        validators=[WhitelistEmailValidator(whitelist=['uni.sydney.edu.au', 'sydney.edu.au'])])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(validators=[WhitelistEmailValidator(whitelist=['uni.sydney.edu.au', 'sydney.edu.au'])])

    class Meta:
        model = User
        fields = ['username', 'email']


# Create a profile update form which will update image attribute in Profile Model
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
