from django.contrib.auth.models import User
from django.db import models

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100, blank=True)
    industry= models.CharField(max_length=100, blank=True)
    company_type=models.CharField(max_length=50, blank=True)
    description=models.TextField(blank=True)
    employee_count=models.IntegerField(null=True, blank=True)
    website=models.CharField(max_length=100, blank=True)
    location=models.CharField(max_length=100, blank=True)
def __str__(self):
    return f"{self.company_name}"

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100, blank=True)
    skills=models.TextField(blank=True)
    experience=models.CharField(max_length=30, blank=True)
    education=models.CharField(max_length=100, blank=True)
    resume=models.FileField(upload_to='resumes/', null=True, blank=True)
    phone=models.CharField(max_length=15, null=True, blank=True)
    desired_role = models.CharField(max_length=100, blank=True)

def __str__(self):
    return f"{self.full_name}"
# Create your models here.
