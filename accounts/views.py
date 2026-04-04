python3 -c "
content = '''from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CompanysignupForm, CandidatesignupForm
from .models import CompanyProfile, CandidateProfile

def company_signup(request):
    if request.method == \"POST\":
        form = CompanysignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data[\"username\"]
            email = form.cleaned_data[\"email\"]
            password = form.cleaned_data[\"password\"]
            company_name = form.cleaned_data[\"company_name\"]
            industry = form.cleaned_data[\"industry\"]
            location = form.cleaned_data[\"location\"]
            if User.objects.filter(username=username).exists():
                form.add_error(\"username\", \"Username already taken\")
                return render(request, \"accounts/company_signup.html\", {\"form\": form})
            user = User.objects.create_user(username=username, email=email, password=password)
            CompanyProfile.objects.create(user=user, company_name=company_name, industry=industry, location=location)
            login(request, user)
            return redirect(\"company_dashboard\")
    else:
        form = CompanysignupForm()
    return render(request, \"accounts/company_signup.html\", {\"form\": form})

def candidate_signup(request):
    if request.method == \"POST\":
        form = CandidatesignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data[\"username\"]
            email = form.cleaned_data[\"email\"]
            password = form.cleaned_data[\"password\"]
            full_name = form.cleaned_data[\"full_name\"]
            phone = form.cleaned_data[\"phone\"]
            skills = form.cleaned_data[\"skills\"]
            desired_role = form.cleaned_data[\"desired_role\"]
            if User.objects.filter(username=username).exists():
                form.add_error(\"username\", \"Username already taken\")
                return render(request, \"accounts/candidate_signup.html\", {\"form\": form})
            user = User.objects.create_user(username=username, email=email, password=password)
            CandidateProfile.objects.create(user=user, full_name=full_name, phone=phone, skills=skills, desired_role=desired_role)
            login(request, user)
            return redirect(\"candidate_dashboard\")
    else:
        form = CandidatesignupForm()
    return render(request, \"accounts/candidate_signup.html\", {\"form\": form})
'''
with open('accounts/views.py', 'w') as f:
    f.write(content)
print('Done!')
"