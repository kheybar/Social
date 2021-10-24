from django import forms


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
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )