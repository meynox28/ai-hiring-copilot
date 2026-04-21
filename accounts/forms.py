from django import forms

class CompanysignupForm(forms.Form):
    username= forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    company_name=forms.CharField(max_length=100)
    industry=forms.CharField(max_length=100)
    location=forms.CharField(max_length=100)
class CandidatesignupForm(forms.Form):
    username= forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    full_name=forms.CharField(max_length=100)
    skills=forms.CharField(widget=forms.Textarea)
    phone=forms.CharField(max_length=30)
    desired_role=forms.CharField(max_length=100)
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    

