from django import forms
from .models import students
from .models import menu
class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'
        labels ={
            'fullname': 'Full Name',
            'email': 'Email Adress',
            'password': 'Password'
        }
class SignInForm(forms.Form):
    fullname = forms.CharField(label='Full Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = menu
        fields = ['menu']  