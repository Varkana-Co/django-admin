from django.shortcuts import render
from django.http import HttpResponse

from .models import Post,Comment

def index(request):
    # bodey
    return HttpResponse('<h1>Hello dear samira</h1>')


def home(request):
    return HttpResponse('<h3>Wellcom to my Website.....</h3>')


def post_list(request):
    post = Post.objects.all()
    context = {'posts':post} 
    return render(request, 'posts/post_list.html', context = context )


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    context ={'post': post, 'comments': comments}
    return render(request, 'posts/post_detail.html', context = context ) 