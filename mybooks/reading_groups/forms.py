from django import forms

class ReadingGroupCreationForm(forms.Form):
  title = forms.CharField()
  capacity = forms.IntegerField()