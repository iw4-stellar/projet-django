from django import forms


class LoginForm(forms.Form):
    identifier = forms.CharField(
        label="Username or email",
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True,
    )
