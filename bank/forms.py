from django import forms
from .models import Account

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address',
              'account_type', 'materials_provided'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(),
            'materials_provided': forms.CheckboxSelectMultiple(choices=Account.MATERIALS_PROVIDED_CHOICES)
        }

