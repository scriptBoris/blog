from django.http      import HttpResponse
from django.template  import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.utils     import timezone
from .models          import Post
from .forms           import PostForm
from .forms           import UserBoxForm

def reg_box(request):
    if request.method=='POST':
        f = UserBoxForm(request.POST)
        if f.is_valid():
            f = form.save(commit=False)
            f.login = request.login
            f.password = request.password
            f.save()
    else:
        form = UserBoxForm(instance=post)
    return render(request, {'form': form} )


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #reg_box(request)
    form = UserBoxForm()
    #render(request,'blog/base.html',{'form': form} )
    return render(request, 'blog/post_list.html', {'posts': posts, 'form':form} )


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

def user_register(request):
    return
