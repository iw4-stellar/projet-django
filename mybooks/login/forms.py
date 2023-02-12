from django import forms


class LoginForm(forms.Form):
    INPUT_ATTRS = {"class": "input input-bordered"}

    identifier = forms.CharField(
        label="Username or email",
        required=True,
        widget=forms.TextInput(INPUT_ATTRS),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(INPUT_ATTRS),
        required=True,
    )
