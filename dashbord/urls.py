from django.urls import path ,include
from .views import dashbord,editBanner,createBanner,deleteBanner,follow

urlpatterns = [
    path('',dashbord),
    path('Follow/',follow),
    path('createBanner/',createBanner),
    path('editBanner/<int:id>',editBanner),
    path('deleteBanner/<int:id>',deleteBanner),
    
]