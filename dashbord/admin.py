from django.contrib import admin
from .models import typeBanner,Banner,UserInfo,Follow
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(typeBanner)
class adminBanner(admin.ModelAdmin):
    list_display = (['type','name','img'])
    
admin.site.register(Banner,adminBanner)


class UserInfoInline(admin.StackedInline):
    model=UserInfo
    can_delete= False
    verbose_name_plural = 'UserInfo'

class CostumUser(UserAdmin):
    inlines = (UserInfoInline,)

admin.site.unregister(User)
admin.site.register(User,CostumUser)

admin.site.register(Follow)


