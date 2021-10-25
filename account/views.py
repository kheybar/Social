from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistarionForm



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request=request, message='you logged in successfully.', extra_tags='success')
                return redirect('posts:posts')
            else:
                messages.error(request=request, message='wrong username or password', extra_tags='warning')
    else:
        form = UserLoginForm()
    
    return render(request, 'account/login.html', {'form': form})



def user_register(request):
    if request.method == 'POST':
        form = UserRegistarionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            messages.success(request=request, message='you register successfully, now login.', extra_tags='success')
            return redirect('posts:posts')
    else:
        form = UserRegistarionForm()

    return render(request, 'account/register.html', {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request=request, message='you logout successfully', extra_tags='success')
    return redirect('posts:posts')



def user_dashboard(request, pk):
    user = get_object_or_404(User, id=pk)
    return render(request, 'account/dashboard.html', {'user': user})