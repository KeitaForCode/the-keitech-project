from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from keitech_app.models import SignUp

class SignUpForm(forms.ModelForm):
    """This will display the SignUp form on the signup page"""
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-style'}))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-style'}))

    class Meta:
        model = SignUp
        fields = '__all__'
        widgets = {
            'First_Name': forms.TextInput(attrs={'class':'input-style'}),
            'Last_Name': forms.TextInput(attrs={'class':'input-style'}),
            'Nick_Name': forms.TextInput(attrs={'class':'input-style'}),
            'email': forms.EmailInput(attrs={'class':'input-style'}),
            'applying_as': forms.Select(attrs={'class':'input-style'})
        }


    def clean(self):
        """This will make sure the password and retype password are the same"""
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        retype_password = cleaned_data.get('retype_password')

        if password != retype_password:
            raise forms.ValidationError("Password and retype_password not match")
