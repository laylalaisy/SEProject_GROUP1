from django import forms
from .models import account

class LoginPostForm(forms.ModelForm):
    class Meta:
        model=account
        fields=('account_id','password')
