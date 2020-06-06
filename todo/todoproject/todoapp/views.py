from django.shortcuts import render,redirect
from .models import Post, Comment
import datetime

# Create your views here.
def home(request):
    posts=Post.objects.all().order_by('duedate')

    return render(request,'home.html',{'posts':posts})


def new(request):
    if request.method=='POST':
        new_post=Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate']
        )
        return redirect('detail',new_post.pk)
    
    return render(request, 'new.html')


def detail(request,post_pk):
    post=Post.objects.get(pk=post_pk)

    if request.method=="POST":
        Comment.objects.create(
            post=post,
            content=request.POST['content']
        )
        return redirect('detail',post_pk)

    return render(request, 'detail.html', {'post':post})


def edit(request,post_pk):
    post=Post.objects.get(pk=post_pk)

    if request.method=='POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            duedate=request.POST['duedate'],
        )
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html',{'post':post})


def delete(request,post_pk):
    post=Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')


def delete_comment(request,post_pk,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)