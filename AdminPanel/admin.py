from django.contrib import admin
from .models import Set_Interview, Check_Interview

# Register your models here.

class SetInterviewAdmin(admin.ModelAdmin):
    list_display = ('interview_name', 'company_name', 'last_date', 'time_limit')
    search_fields = ('interview_name', 'company_name')
    list_filter = ('last_date')

class CheckInterviewAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'email_id', 'profile', 'gender', 'age', 'status_after_interview', 'applied_on', 'interview_details')
    search_fields = ('candidate_name', 'email_id')
    list_filter = ('status_after_interview', 'applied_on')

admin.site.register(Set_Interview, SetInterviewAdmin)
admin.site.register(Check_Interview, CheckInterviewAdmin)
