from django.shortcuts import render

# Create your views here.

def music(request):
    return render(request,'music.html')
