from django.contrib import admin
from .models import item,category,likeItem
# Register your models here.
admin.site.register(item)
class Category(admin.ModelAdmin):
    list_display = (['name'])
    
    
admin.site.register(category,Category)
admin.site.register(likeItem)

