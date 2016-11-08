from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post, Comment, Like
from .forms import Post_Form

# General BLog views
def Blog(request):
    posts = Post.objects.all().order_by('-Posted_Date')
    return render(request, 'Blog/Blog.html', {'Posts' : posts})

def Post_Page(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    comments = Comment.objects.filter(Post__pk = post_id)
    isLiked = post.isLiked(request.user.pk)

    return render(request, 'Blog/Post.html', {'Post' : post,'isLiked' :isLiked, 'Comments': comments})

def Like_Post(request, post_id):
    Post.objects.filter(pk = post_id)[0].like(request.user.pk)
    return redirect('blog:post', post_id = post_id)

def Dislike_Post(request, post_id):
    Post.objects.filter(pk = post_id)[0].dislike(request.user.pk)
    return redirect('blog:post', post_id = post_id)


# Institutes interface
def My_Posts(request):
    My_Posts = Post.objects.filter(User = request.user).order_by('-Posted_Date')
    return render(request, 'Blog/My_Posts.html', {'Posts' : My_Posts})

def Create_Post(request):
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.User = User.objects.filter(pk = request.user.pk)[0]
            post.save()

            return redirect('blog:post', post_id = post.pk)
    else:
        form = Post_Form()
    return render(request, 'Blog/Create_Post.html', {'form': form})

def Edit_Post(request, post_id):
    return render(request, 'Blog/Create_Post.html')