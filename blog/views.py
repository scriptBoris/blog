from django.template  import *
from django.http      import HttpResponse
from django.contrib   import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils     import timezone
from django.core.paginator import Paginator
from .models          import Post
from .forms           import PostForm

def post_list(request, page_num=1):
    posts = Post.objects.all().order_by('-created_date') #filter(created_date__lte=timezone.now()).order_by('-created_date')
    current_page = Paginator(posts, 7)
    return render(request, 'blog/post_list.html', {'posts': current_page.page(page_num)} )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post} )

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form} )

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form} )

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).delete()
    return redirect('post_list')

def register(request):
    error = ""
    if request.method == "POST":
        user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['password'] )
        user.save()
        if user == None:
            error = "Ошибка"
        else:
            auth.authenticate(username=request.POST['login'], password=request.POST['password'])
            auth.login(request, user)
            return redirect("/user/"+user.username)
        return render(request, 'blog/register.html', {'error': error} )
    return render(request, 'blog/register.html', {'error': error} )

def login(request):
    login = request.POST['login']
    password = request.POST['password']
    user = auth.authenticate(username=login, password=password)
    if user is not None:
        auth.login(request, user)
    return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect("/")

def user(request, name):
    user = User.objects.get(username=name)
    return render(request, 'blog/user.html', {'user': user} )
