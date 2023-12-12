from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from django.contrib.auth.models import User

from .models import Teacher, TeacherProfile


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = "teacher"

class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False
    verbose_name_plural = "teacher_profile"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [TeacherInline, TeacherProfileInline]



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)