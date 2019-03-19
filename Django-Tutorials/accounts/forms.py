from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import UserProfile


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'tabindex': 1}), required=True)
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address', 'tabindex': 1}), required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'tabindex': 2}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'tabindex': 2}))


    class Meta:
        model = User
        fields = (
            'username',
            # 'first_name',
            # 'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = (
            'image',
        )
