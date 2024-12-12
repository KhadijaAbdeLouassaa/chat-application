from django.urls import path
from . import views

app_name = "chats"

urlpatterns = [
    
    path('', views.chat, name = "chat"),
    path('chat/<str:username>/', views.chat_detail, name = "chat_detail"),
   
]
