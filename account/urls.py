from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('login/phone/', views.phone_login, name='phone_login'),
    path('login/phone/verify/', views.phone_login_verify, name='phone_login_verify'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/<int:pk>', views.user_dashboard, name='dashboard'),
    path('dashboard/profile_edit/<int:pk>', views.profile_edit, name='profile_edit'),
]