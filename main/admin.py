from django.contrib import admin
from .models import FeedbackModel
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['email', 'message']
    
    
admin.site.register(FeedbackModel, FeedbackAdmin)