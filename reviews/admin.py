from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug', 'timestamp', 'updated']
    search_fields = ['title', 'content']

admin.site.register(Review, ReviewAdmin)