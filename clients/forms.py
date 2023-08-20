from .models import Client
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ClientForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last name'}), label='')
    address1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address1'}), label='')
    address2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address2'}), label='', required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city'}), label='')
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'state'}), label='')
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'zipcode'}), label='')
    phone = PhoneNumberField()
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'email'}), label='')
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'notes'}), label='')

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'phone', 'email',
                  'notes']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['last_name'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['address1'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['address2'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['city'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['state'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['zipcode'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['phone'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['email'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
        self.fields['notes'].widget.attrs[
            'class'] = 'w-full border-b border-gray-400 text-gray-800 focus:outline-none'
