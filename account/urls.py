from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/<int:pk>', views.user_dashboard, name='dashboard'),
    path('dashboard/profile_edit/<int:pk>', views.profile_edit, name='profile_edit'),
]