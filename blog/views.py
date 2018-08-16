from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.models import Post_board
from .forms import PostForm
from django.shortcuts import redirect
from blog.forms import Post_board_Form
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return render(request,'blog/main.html',{})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    form = PostForm()
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})

@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
            form = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



def post_board_list(request):
    posts = Post_board.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_board_list.html',{'posts':posts})

def post_board_detail(request,pk):
    post = get_object_or_404(Post_board,pk=pk)
    return render(request, 'blog/post_board_detail.html',{'post':post})

@login_required
def post_board_new(request):
    form = Post_board_Form()
    if request.method == "POST" :
        form = Post_board_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_board_detail',pk=post.pk)
    else:
        form = Post_board_Form()
    return render(request, 'blog/post_board_edit.html',{'form':form})

@login_required 
def post_board_edit(request,pk):
    post = get_object_or_404(Post_board,pk=pk)
    if request.method =="POST":
        form = Post_board_Form(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_board_detail',pk=post.pk)
    else:
            form = Post_board_Form(instance=post)
    return render(request,'blog/post_board_edit.html',{'form':form})

@login_required
def post_board_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_board_list')
