from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth 
from django.contrib.auth  import get_user_model
User = get_user_model()
from .forms import register,createBannerForm
from items.models import item,category
from .models import Banner,typeBanner,UserInfo,Follow
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request):
    cat = category.objects.all()
    type = typeBanner.objects.filter(name='mainBanner').first()
    mainBanner = Banner.objects.filter(type=type)
    type = typeBanner.objects.filter(name='offBanner').first()
    offBanner = Banner.objects.filter(type=type)
    return render(request,'main.html',{
        'category':cat,
        'mainBanner':mainBanner,
        'offBanner':offBanner
        })

def profile(request,name):
    user = get_object_or_404(User,username=name)
    items = item.objects.filter(created_by=user)
    followers = len(Follow.objects.filter(user=user))
    following = len(Follow.objects.filter(follower=user))
    followed = Follow.objects.filter(user=user,follower = request.user)
    return render(request,'profile.html',{'user':user,'items':items,'followers':followers,'following':following,'followed':followed})

@login_required(login_url='/login')
def dashbord(request):
    banner = Banner.objects.all()
    myItems = item.objects.filter(created_by=request.user)
    return render(request,'dashbord.html',{'myItems':myItems,'banner':banner})

@login_required(login_url='/login')
def userEdit(request):
    info = get_object_or_404(UserInfo,user=request.user)
    if request.method == 'POST':
                info.gender = request.POST['gender']
                info.bio = request.POST['bio'] or info.bio
                info.profile = request.FILES.get('profile') or info.profile
                info.github = request.POST['github']
                info.telegram = request.POST['telegram']
                info.website = request.POST['website']
                info.instagram = request.POST['instagram']
                info.save()
                return redirect('/dashbord')    
    return render(request,'editUser.html',{'info':info})


def creatUser(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username = request.POST['username'])
            userinfo =  UserInfo.objects.create(user=user)
            userinfo.save()
            return redirect('/login/')
    else:
        form = register()
    return render(request,'register.html',{'form':form})

@login_required(login_url='/login')
def logOut(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login')
def follow(request):
    user = request.GET.get('follow')
    fol = Follow.objects.filter(user=user,follower=request.user.username).first()
    if fol:
        fol.delete()
    else:
        fol = Follow.objects.create(user=user,follower=request.user.username)
        fol.save()
    return redirect(f'/profile/{user}')

















@login_required
def createBanner(request):
    if request.method == 'POST':
        form = createBannerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashbord/')
    else:
        form = createBannerForm()
    return render(request,'Banner/createBanner.html',{'form':form,'title':'Create new Banner'})

@login_required
def editBanner(request,id):
    oldBanner = get_object_or_404(Banner,id=id)
    if request.method == 'POST':
        form = createBannerForm(request.POST,request.FILES,instance=oldBanner)
        if form.is_valid():
            form.save()
            return redirect('/dashbord/')
    else:
        form = createBannerForm(instance=oldBanner)
    return render(request,'Banner/createBanner.html',{'form':form,'title':'Edit a Banner'})

@login_required
def deleteBanner(request,id):
    dBanner =  Banner.objects.filter(id=id)
    dBanner.delete()
    return redirect('/dashbord/')

