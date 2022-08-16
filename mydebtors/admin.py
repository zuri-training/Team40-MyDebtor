from django.contrib import admin
from .models import*
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'school']
    ordering = ['first_name','last_name','school']
    list_per_page = 10
    search_fields = ['first_name__istartswith','last_name__istartswith','school__istartswith']


admin.site.register(Student, StudentAdmin)
admin.site.register(Sponsor)

admin.site.register(Debt)  

def hello():
    pass