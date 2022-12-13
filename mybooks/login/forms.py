from django import forms

class BooksellerRegistrationForm(forms.Form):
  email = forms.EmailField(
    label="Email",
    widget=forms.EmailInput,
  )
  password = forms.CharField(
    label="Password",
    widget=forms.PasswordInput,
    max_length=16,
  )

class ClientRegistrationForm(forms.Form):
  email = forms.EmailField(
    label="Email",
    widget=forms.EmailInput,
  )
  password = forms.CharField(
    label="Password",
    widget=forms.PasswordInput,
    max_length=16,
  )
