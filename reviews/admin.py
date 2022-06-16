from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['title']

admin.site.register(Review, ReviewAdmin)