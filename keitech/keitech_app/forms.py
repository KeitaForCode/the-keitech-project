from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from keitech_app.models import SignUp, Contacts, NewsLetter


class ContactForm(forms.ModelForm):
    """This will display the contact form on the contact us page"""

    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'contact-form'}),
            'email': forms.EmailInput(attrs={'class':'contact-form'}),
            'comments': forms.Textarea(attrs={'class':'contact-form'}),
        }


class NewsLetterForm(forms.ModelForm):
    """this will manage the newsleter form on the homepage"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'newsletter-input', 'placeholder':'Enter your email address'}), label='')

    class Meta:
        model = NewsLetter
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class':'newsletter-input'}),
        }




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
            'Phone': forms.NumberInput(attrs={'class':'input-style'}),
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
