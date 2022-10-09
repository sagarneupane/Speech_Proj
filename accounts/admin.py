from django.contrib import admin
from accounts.models import MyUser

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id","username","name","email","date_of_birth","phone_number","age","is_active"]