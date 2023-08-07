"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from dashbord.views import main
from django.conf import settings
from dashbord.views import creatUser,logOut,userEdit,profile
from django.contrib.auth import views as auth_views
from dashbord.forms import login

urlpatterns = [
    path('', main),
    path('profile/<str:name>',profile),
    path('register/',creatUser),
    path('logout/',logOut),
    path('userEdit/',userEdit),
    path('login/',auth_views.LoginView.as_view(authentication_form=login,template_name='login.html')),
    path('admin/', admin.site.urls),
    path('dashbord/', include('dashbord.urls')),
    path('items/', include('items.urls')),
    path('music/', include('music.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
