from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import AddPostForm, EditPostForm, AddCommentForm, AddReplyForm


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {'posts': posts})



def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day, slug=slug)
    comments = Comment.objects.filter(post=post, is_reply=False)
    reply_form = AddReplyForm()
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'your comment submitted', 'success')
            form = AddCommentForm()
    else:
        form = AddCommentForm()

    return render(request, 'posts/post_detail.html', {'post':post, 'comments':comments, 'form': form, 'reply': reply_form})



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



@login_required
def delete_post(request, pk, post_id):
	if request.user.id == pk:
		Post.objects.filter(id=post_id).delete()
		messages.success(request, 'your post deleted successfully', 'success')
		return redirect('account:dashboard', pk)
	else:
		return redirect('posts:posts')



@login_required
def edit_post(request, pk, post_id):
	if request.user.id == pk:
		post = get_object_or_404(Post, id=post_id)
		if request.method == 'POST':
			form = EditPostForm(request.POST, instance=post) # برای اینکه جنگو بقیه ی مقادیر رو از اینستس بگیره، بهش خود اینستنس رو میدیم
			if form.is_valid():
				new_post = form.save(commit=False)
				new_post.slug = slugify(form.cleaned_data['body'][:30])
				new_post.save()
				messages.success(request, 'your post updated successfully', 'success')
				return redirect('account:dashboard', pk)
		else:
			form = EditPostForm(instance=post)
		return render(request, 'posts/edit_post.html', {'form': form})
	else:
		return redirect('posts:posts')



@login_required
def reply_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = AddReplyForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.user = request.user
            new_reply.post = post
            new_reply.reply = comment
            new_reply.is_reply = True
            new_reply.save()
            messages.success(request, 'your reply save successfully', 'success')

    return redirect('posts:post_detail', post.created.year, post.created.month, post.created.day, post.slug)