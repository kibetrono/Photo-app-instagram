from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('',views.index,name='index'),
    path('myimages',views.my_images,name="my_images"),
    path('upload/', views.uploadPicture, name='profile'),
    path('comments/<int:pk>/', views.comment, name='comment'),
    path('like/<int:id>/', views.like_picture, name='like'),
    path('each/<int:id>/', views.each_image, name='eachimage'),
    path('search/', views.search, name='search'),

]