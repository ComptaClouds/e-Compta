
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm,UserChangeForm




class RegistrationForm(UserCreationForm,forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username',
                 'email',
                 'password1',
                 'password2',
                 )



class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class HomeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('raison_social',
                  'contact',
                  'logo'
                  )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('raison_social',
                  'contact',
                  'logo')