from django.urls import path
from . import views

urlpatterns = [
    path('signup/company', views.company_signup, name='company_signup'),
    path('signup/candidate', views.candidate_signup, name='candidate_signup'),
]
