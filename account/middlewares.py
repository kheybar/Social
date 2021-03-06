from django.shortcuts import redirect
from django.contrib import messages



LOGIN_EXEMPT_URLS = [
    '/',
    '/account/login/',
    '/account/login/phone/',
    '/account/login/phone/verify/',
    '/account/register/',
]



class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in LOGIN_EXEMPT_URLS:
            return redirect('account:login')
        response = self.get_response(request)

        return response
