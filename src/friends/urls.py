from django.urls import path
from . import views

app_name = "friends"

urlpatterns = [
    
    path('search/', views.search_friend, name = "search"),
    path('notification/', views.notification, name = "notification"),

    path('follow/<str:username>/', views.follow, name = "follow"),
    path('unfollow/<str:username>/', views.unfollow, name = "unfollow"),
    
    path('accept_follower/<str:username>/', views.accept_follower, name = "accept_follower"),
    path('remove_follower/<str:username>/', views.remove_follower, name = "remove_follower"),
]
