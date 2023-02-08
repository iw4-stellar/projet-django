from django import forms


class BooksellerRegistrationForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput,
        max_length=255,
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput,
        max_length=255,
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        max_length=16,
        required=True,
    )
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput,
        max_length=16,
        required=True,
    )


class ClientRegistrationForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput,
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        max_length=16,
        required=True,
    )
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput,
        max_length=16,
        required=True,
    )
