from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import AddPostForm


def all_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/all_posts.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, 
        created__year=year,
        created__month=month,
        created__day=day,
        slug=slug,
        )

    return render(request, 'posts/post_detail.html', {'post': post})



@login_required
def add_post(request, pk):
	if request.user.id == pk:
		if request.method == 'POST':
			form = AddPostForm(request.POST)
			if form.is_valid():
				new_post = form.save(commit=False)
				new_post.user = request.user
				new_post.slug = slugify(form.cleaned_data['body'][:30])
				new_post.save()
				messages.success(request, 'your post submitted', 'success')
				return redirect('account:dashboard', pk)
		else:
			form = AddPostForm()
		return render(request, 'posts/add_post.html', {'form':form})
	else:
		messages.success(request, 'you cant send post', 'danger')
		return redirect('posts:posts')