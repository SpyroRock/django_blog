from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
from .models import Post

# User = get_user_model()

@login_required
def post_create_view(request):
    if request.method == "POST":
        context = {}
        title = request.POST['title']
        content = request.POST['content']

        if title and content:
            user = request.user
            post = Post.objects.create(title=title, content=content, author=user)
            return redirect('posts:detail', pk=post.id)
        else:
            context['error'] = "Title and Content Fields cannot be empty"
            return render(request, 'posts/create.html', context=context)
    else:
        return render(request, 'posts/create.html')

# View one specific blog post
def post_detail_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    context = {'post': post}
    return render(request, 'posts/detail.html', context=context)

# View all blog posts
def post_list_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/list.html', context=context)

# Update one specifi post
@login_required
def post_update_view(request, pk):
    context = {}
    post =Post.objects.filter(id=pk).first()
    context['post']=post
    if request.user == post.author or request.user.is_superuser:
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']

            if title and content:
                post.title = title
                post.content = content
                post.save()
                # context['error'] = "No errors. Your post has been updated"
                return render(request, 'posts/update.html', context=context)
            else:
                context['error'] = "Title and Content Fields cannot be empty"
                return render(request, 'posts/update.html', context=context)
        else:
            return render(request, 'posts/update.html', context=context)
    else:
        return redirect('posts:list')

# Delete one specific post
@login_required
def post_delete_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    if request.user == post.author or request.user.is_superuser:
        if request.method == "POST":
            post.delete()
            return redirect('posts:list')
        else:
            return render(request, 'posts/delete.html')
    else:
        return redirect('posts:list')