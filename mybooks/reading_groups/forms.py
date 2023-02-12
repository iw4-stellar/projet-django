from django import forms


class ReadingGroupCreationForm(forms.Form):
    INPUT_ATTRS = {
        "class": "input input-bordered",
    }
    TEXTAREA_ATTRS = {
        "class": "input input-bordered h-36",
        "rows": 5,
    }

    title = forms.CharField(
        widget=forms.TextInput(INPUT_ATTRS),
        required=True,
    )
    capacity = forms.IntegerField(
        widget=forms.NumberInput(INPUT_ATTRS),
        required=True,
    )

    description = forms.CharField(
        widget=forms.Textarea(TEXTAREA_ATTRS),
        required=False,
    )
