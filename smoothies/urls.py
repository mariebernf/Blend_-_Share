from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.smoothie_list, name='smoothie_list'),
    path('create/', views.smoothie_create, name='smoothie_create'),
    path('update/<int:pk>/', views.smoothie_update, name='smoothie_update'),
    path('<int:pk>/edit/', views.smoothie_update, name='smoothie_edit'),
    path('delete/<int:pk>/', views.smoothie_delete, name='smoothie_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('accounts/profile/', lambda request: redirect('smoothie_list')),
]
