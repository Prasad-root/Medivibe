from django import forms
from django.contrib.auth.models import User
from .models import Profile

class CustomUserRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Full Name'
    }))
    home_address = forms.CharField(max_length=500, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Home Address'
    }))
    contact_number = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contact Number'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['email'],  # Use email as username
            email=self.cleaned_data['email']
        )
        user.set_password(self.cleaned_data['password1'])  # Hash password
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                home_address=self.cleaned_data['home_address'],
                contact_number=self.cleaned_data['contact_number']
            )
        return user
