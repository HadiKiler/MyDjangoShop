from django.urls import path
from .views import items,newItem,details,deleteItem,editItem,Like

urlpatterns = [
    path('',items),
    path('newItem/',newItem),
    path('details/<int:id>',details),
    path('deleteItem/<int:id>',deleteItem),
    path('editItem/<int:id>',editItem),
    path('like/',Like)
]