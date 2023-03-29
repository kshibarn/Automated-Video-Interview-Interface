from django.db import models
from django.core.validators import EmailValidator

# Create your models here.

class Set_Interview(models.Model):
    interview_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    last_date = models.DateField()
    questions = models.TextField()
    time_limit = models.IntegerField()

    def __str__(self):
        return self.interview_name
    
class Check_Interview(models.Model):
    candidate_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255, validators=[EmailValidator()])
    profile = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    age = models.PositiveIntegerField()
    interview = models.ForeignKey(Set_Interview, on_delete=models.CASCADE)
    status_after_interview = models.CharField(max_length=255, blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    interview_details = models.TextField(blank=True)

    def __str__(self):
        return self.candidate_name