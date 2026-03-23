from django.db import models
# Create your tests here.
class Job(models.Model):
    title=models.CharField(max_length=100)
    company_name= models.CharField(max_length=100)
    company_description=models.TextField()
    job_type=models.CharField(max_length=50)
    vacancies=models.IntegerField()
    required_skills=models.TextField()
    salary=models.CharField(max_length=30)
    deadline=models.DateField()
    experience_required=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    posted_at=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"{self.title} at {self.company_name}"
        

# Create your models here.
