from django import forms
from django.core.exceptions import ValidationError
from users.models import User


class BooksellerRegistrationForm(forms.Form):
    INPUT_ATTRS = {"class": "input input-bordered"}

    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(INPUT_ATTRS),
        max_length=255,
        required=True,
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(INPUT_ATTRS),
        max_length=255,
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(INPUT_ATTRS),
        max_length=255,
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(INPUT_ATTRS),
        max_length=16,
        required=True,
    )
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(INPUT_ATTRS),
        max_length=16,
        required=True,
    )

    def clean(self):
        data = super().clean()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Passwords don't match")

        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            self.add_error("username", "Username already in use")

        email_exists = User.objects.filter(email=email)
        if email_exists:
            self.add_error("email", "Email address already in use")

        return data


class ClientRegistrationForm(forms.Form):
    INPUT_ATTRS = {"class": "input input-bordered"}

    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(INPUT_ATTRS),
        required=True,
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(INPUT_ATTRS),
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(INPUT_ATTRS),
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(INPUT_ATTRS),
        max_length=16,
        required=True,
    )
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(INPUT_ATTRS),
        max_length=16,
        required=True,
    )

    def clean(self):
        data = super().clean()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Passwords don't match")

        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            self.add_error("username", "Username already in use")

        email_exists = User.objects.filter(email=email)
        if email_exists:
            self.add_error("email", "Email address already in use")

        return data
