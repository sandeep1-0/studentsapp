from django import forms
from students.models import *
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    # username = forms.CharField(max_length=150)
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match")

class fulldetails(forms.ModelForm):

    class Meta:
        model = details
        fields = ['firstname','lastname','student_dpt','student_img']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
