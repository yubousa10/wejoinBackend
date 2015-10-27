from django.contrib import admin
from .models import *

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    pass

class UserBaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Register,RegisterAdmin)
admin.site.register(UserBase,UserBaseAdmin)