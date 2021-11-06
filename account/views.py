from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserLoginForm, PhoneLoginForm, PhoneLoginVerifyForm, UserRegistarionForm, EditProfileForm
from posts.models import Post
from .models import Profile, Relational
from random import randint
from kavenegar import *



def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request=request, message='you logged in successfully.', extra_tags='success')
                if next:
                    return redirect(next)
                return redirect('posts:posts')
            else:
                messages.error(request=request, message='wrong username or password', extra_tags='warning')
    else:
        form = UserLoginForm()
    
    return render(request, 'account/login.html', {'form': form})


def phone_login(request):
	if request.method == 'POST':
		form = PhoneLoginForm(request.POST)
		if form.is_valid():
			global phone, rand_num
			phone = f"0{form.cleaned_data['phone']}"
			rand_num = randint(1000, 9999)
			api = KavenegarAPI('6A3948423067466E74556D4C776B7A4458592B737A67665936556437614A30316D6F5A334A7436435173673D') 
			message = f'کد ورود شما به شبکه اجتماعی سوشیال {rand_num}'
			params = { 'sender' : '10008663', 'receptor': phone, 'message':message} 
			response = api.sms_send(params)
			return redirect('account:phone_login_verify')
	else:
		form = PhoneLoginForm()
	return render(request, 'account/login_phone.html', {'form':form})



def phone_login_verify(request):
	if request.method == 'POST':
		form = PhoneLoginVerifyForm(request.POST)
		if form.is_valid():
			if rand_num == form.cleaned_data['code']:
				profile = get_object_or_404(Profile, phone=phone)
				user = get_object_or_404(User, profile__id=profile.id)
				login(request, user)
				messages.success(request, 'logged in successfully', 'success')
				return redirect('posts:posts')
			else:
				messages.error(request, 'your code is wrong', 'warning')
	else:
		form = PhoneLoginVerifyForm()
    
	return render(request, 'account/phone_login_verify.html', {'form': form})




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



@login_required # if user not login, redirect to settings.LOGIN_URL(default: 'accounts/login')
def user_logout(request):
    logout(request)
    messages.success(request=request, message='you logout successfully', extra_tags='success')
    return redirect('posts:posts')



@login_required
def user_dashboard(request, pk):
    user = get_object_or_404(User, id=pk)
    posts = Post.objects.filter(user=user).order_by('-created')
    relational = Relational.objects.filter(from_user=request.user.id, to_user=user)
    self_dashboard = False
    is_following = False
    if request.user.id == pk:
        self_dashboard = True
    if relational.exists():
        is_following = True
    return render(request, 'account/dashboard.html', {'user': user, 'posts': posts, 'self_dashboard': self_dashboard, 'is_following': is_following})



# برای اینکه کاربر بتونه پروفایلش رو آپدیت کنه، چون ما داریم از پروفایل و یوزر استفاده میکنیم،
# روش یکم فرق داره
@login_required
def profile_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST ,instance=user.profile)
        if form.is_valid():
            form.save()
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'your profile edit successfully', extra_tags='success')
            return redirect('account:dashboard', pk)
    else:
        form = EditProfileForm(instance=user.profile, initial={'email': request.user.email}) # initial: یک دیکشنری هست که میتونیم برای فیلدهامون مقدار اولیه قرار بدیم. فرقش با اینستنس اینه که میتونیم خودمون تغییرش بدیم

    return render(request, 'account/edit_profile.html', {'form': form})




@login_required
def follow(request):
    if request.method == 'POST':
        user_id = request.POST['user_id'] # get user_id from Jquery
        following = get_object_or_404(User, pk=user_id) # یوزری که میخوایم فالوش کنیم
        check_relation = Relational.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            return JsonResponse({'status': 'exists'})

        else:
            Relational(from_user=request.user, to_user=following).save()
            return JsonResponse({'status': 'ok'})




@login_required
def unfollow(request):
    if request.method == 'POST':
        user_id = request.POST['user_id'] # get user_id from Jquery
        following = get_object_or_404(User, pk=user_id) # یوزری که میخوایم فالوش کنیم
        check_relation = Relational.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            check_relation.delete()
            return JsonResponse({'status': 'ok'})

        else:
            return JsonResponse({'status': 'not_exists'})