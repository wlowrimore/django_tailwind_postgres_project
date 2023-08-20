from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import CustomUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-full border-b border-gray-700 px-1 focus:outline-none', 'placeholder': 'first name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-full border-b border-gray-700 px-1 focus:outline-none', 'placeholder': 'last name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'w-full border-b border-gray-700 px-1 focus:outline-none', 'placeholder': 'email address'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'w-full border-b border-gray-700 px-1 focus:outline-none', 'placeholder': '**********'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'w-full border-b border-gray-700 px-1 focus:outline-none', 'placeholder': 'confirm password'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    #
    #     def __init__(self, *args, **kwargs):
    #         super(SignUpForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['email'].widget.attrs['class'] = 'border-b border-700'
    #     self.fields['email'].widget.attrs['placeholder'] = 'email address'
    #     self.fields['email'].label = ''
    #     self.fields[
    #         'email'].help_text = None
    #
    #     self.fields['password1'].widget.attrs['class'] = 'border-b border-gray-700 bg-red-400'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'password'
    #     self.fields['password1'].label = ''
    #     self.fields[
    #         'password1'].help_text = None
    #
    #     self.fields['password2'].widget.attrs['class'] = 'border-b border-gray-700'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
    #     self.fields['password2'].label = ''
    #     self.fields[
    #         'password2'].help_text = None
