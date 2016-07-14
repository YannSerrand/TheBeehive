
from django import forms
from django.core.exceptions import ValidationError


class AccountForm(forms.Form):
    
    def __init__(self, *args,**kwargs):
        
        super(AccountForm, self).__init__(*args,**kwargs)
                
        self.fields['username'] = forms.CharField(required=True)
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['last_name'] = forms.CharField(required=True)
        self.fields['email'] = forms.EmailField(required=True)
        self.fields['password'] = forms.CharField(required=True, widget=forms.PasswordInput)
        self.fields['confirm_password'] = forms.CharField(required=True, widget=forms.PasswordInput)
        
    def clean(self):
        
        cleaned_data = super(AccountForm, self).clean()
        
        #first cleaning
        
        pwd = cleaned_data.get("password")
        confirm_pwd = cleaned_data.get("confirm_password")        
        if pwd != confirm_pwd:
            
            raise ValidationError('Passwords are not the same.')
        
        return cleaned_data