from django.contrib import admin
from .models import Student,Course,Contact

class StudentAdmin(admin.ModelAdmin):
  list_display = ("id", "fName", "lName",)
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
  list_display = ("id", "cName", "isFinished",)
admin.site.register(Course, CourseAdmin)

class ContactAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "number", "gender",)
admin.site.register(Contact, ContactAdmin)