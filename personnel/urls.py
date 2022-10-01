from django.urls import path
from .views import handel_registeration
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('register-user/', handel_registeration, name = 'user-registeration'),
    path('', auth_views.LoginView.as_view(template_name=  'personnel/login.html'), name= 'user_login'),
    path("logout/",auth_views.LogoutView.as_view(template_name = 'personnel/logout.html'), name = 'user-logout'),

]