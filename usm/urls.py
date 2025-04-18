from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('create-post/', views.create_post, name='create_post'),

]
