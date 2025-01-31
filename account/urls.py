from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.rigesteruser.as_view(), name='register'),
    path('login/', views.loginuser.as_view(), name='login'),
    path('logout/', views.logoutuser.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.profileuser.as_view(), name='profile'),
]