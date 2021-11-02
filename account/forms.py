from django import forms
from .models import Profile

email_messages = {
    'required': 'این فیلد اجباری است',
    'invalid': 'لطفا یک ایمیل معتبر وارد کنید',
    'max_length': 'تعداد کارکتر ها بیش از حد مجاز است'
}


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'username'}
            )
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )



class UserRegistarionForm(forms.Form):
    username = forms.CharField(
        label='username',
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'username'}
            )
    )
    email = forms.EmailField(
        label='email',
        max_length=50,
        error_messages=email_messages,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )



class EditProfileForm(forms.ModelForm):
    email = forms.EmailField() # Add Dynamical Field
    class Meta:
        model = Profile
        fields = ('bio', 'age')