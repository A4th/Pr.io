from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 
                                                                           'placeholder': '...Input valid email'}))
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'input-field'
                                                                                              ,'placeholder': '...Input FIRST name'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'input-field',
                                                                                             'placeholder': '...Input LAST name'}))
    is_active = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'check-field'}))
    is_staff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'check-field'}))
    is_superuser = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'check-field'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                   'password1', 'password2', 'is_active', 'is_staff',
                   'is_superuser')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['username'].widget.attrs['placeholder'] = '...Input username'

        self.fields['password1'].widget.attrs['class'] = 'input-field'
        self.fields['password1'].help_text = None
        self.fields['password1'].widget.attrs['placeholder'] = '...Input password'

        self.fields['password2'].widget.attrs['class'] = 'input-field'
        self.fields['password2'].help_text = None
        self.fields['password2'].widget.attrs['placeholder'] = '...Confirm password'



