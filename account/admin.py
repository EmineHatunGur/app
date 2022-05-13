from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel


class CustomAdmin(UserAdmin):
   
    list_display=('username','email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar değiştirme alanı', {
           "fields": ['avatar'],
        }),
    )
   
    


admin.site.register(CustomUserModel,CustomAdmin)