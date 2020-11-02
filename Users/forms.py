from django import forms
from Users.models import User
class Userprofile(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'
