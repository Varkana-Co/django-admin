from django import forms


class PostForms(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    is_enable = forms.BooleanField()
    publish_date = forms.DateField()

