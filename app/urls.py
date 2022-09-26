from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),  
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name="home"),
	path("profile/", views.profile, name='profile'),
	path('add/', views.add, name='add'),
	path('drugs/<str:pk>/', views.drug, name='drug'),
	path('delete/<str:pk>/', views.delete, name='delete'),
]