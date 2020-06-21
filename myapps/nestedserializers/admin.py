from django.contrib import admin
from .models import Student, Marks


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    pass


class MarksAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.site_header = 'Haritha Computers & Technology'
