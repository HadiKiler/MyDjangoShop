from django.shortcuts import render,redirect ,get_object_or_404
from .models import item,category,likeItem
from .forms import newItemForm,editItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def items (request):
    likes = likeItem.objects.filter(username=request.user.username)
    items = item.objects.all()
    cat = category.objects.all()

    likedItems = []
    for i in items:
        for like in likes:
            if i.id == like.post_id:
                likedItems.append(i.id)


    typeActive = request.GET.get('typeActive',0)
    Skey = request.GET.get('Skey','')
    if Skey:
        items = item.objects.filter(Q(name__icontains=Skey)|Q(dis__icontains=Skey))
    if typeActive:
        if Skey:
            items = item.objects.filter(Q(type=typeActive)&(Q(name__icontains=Skey)|Q(dis__icontains=Skey)))
        else:
            items = item.objects.filter(type=typeActive)
    return render(request,'item.html',{
        'items':items,
        'category':cat,
        'typeActive':int(typeActive),
        'Skey':Skey,
        'likedItems':likedItems
        })

def details(request,id):
    ditem = get_object_or_404(item,id=id)
    return render(request,'details.html',{'item':ditem})

@login_required
def newItem(request):
    if request.method == 'POST':
        form = newItemForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect(f'/items/details/{form.id}')
    else:
        form = newItemForm()
    return render(request,'newItems.html',{'form':form})

@login_required
def editItem(request,id):
    oldItem = get_object_or_404(item,id=id,created_by=request.user)
    if request.method == 'POST':
        form = editItemForm(request.POST,request.FILES,instance=oldItem)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect(f'/items/details/{form.id}')
    else:
        form = editItemForm(instance=oldItem)
    return render(request,'newItems.html',{'form':form})


@login_required
def deleteItem(request,id):
    ditem = get_object_or_404(item,id=id)
    ditem.delete()
    return redirect('/items/')

def Like(request):
    post_id = request.GET.get('post_id')
    username = request.user.username
    post = get_object_or_404(item,id=post_id)
    like = likeItem.objects.filter(username=username,post_id=post_id)
    if like:
        like.delete()
        post.likes -=1
        post.save()
    else:
        like = likeItem.objects.create(username=username,post_id=post_id)
        like.save()
        post.likes +=1
        post.save()
    return redirect('/items')