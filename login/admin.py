from django.contrib import admin

# Register your models here.

from . import models
from login.models import User,ConfirmString


# admin.site.register(models.User)

@admin.register(User)
class LoginAdmin(admin.ModelAdmin):
    # 展示信息
    list_display = ['name', 'sex', 'c_time']

    # 搜索框
    search_fields = ['name', 'sex']

    # 过滤器
    list_filter = ['c_time', 'sex']

admin.site.register(models.ConfirmString)


