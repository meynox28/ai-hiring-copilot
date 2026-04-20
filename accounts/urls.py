from django.urls import path
from . import views

urlpatterns = [
    path('signup/company', views.company_signup, name='company_signup'),
    path('signup/candidate', views.candidate_signup, name='candidate_signup'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('signup/company', views.company_signup, name='company_signup'),
    path('signup/candidate', views.candidate_signup, name='candidate_signup'),
    path('dashboard/company', views.company_dashboard, name='company_dashboard'),
    path('dashboard/candidate', views.candidate_dashboard, name='candidate_dashboard'),
]