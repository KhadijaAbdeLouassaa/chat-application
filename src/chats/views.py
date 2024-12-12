from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from friends.models import Friend
from chats.models import ChatRoom
from django.db.models import Q
# Create your views here
# '''
@login_required
def chat(request):
    user = request.user
    friends = Friend.objects.filter(Q(following=user)|Q(follower=user), is_accepted=True)
    
    for friend in friends :
        if friend.following == user:
            friend.unread_msg = ChatRoom.objects.filter(receiver = user, sender=friend.follower, unread_messages=False).count()
            try :
            
                friend.last_message_added =  ChatRoom.objects.filter(Q(sender=friend.follower, receiver=user)|Q(sender=user, receiver=friend.follower)).latest('timestamp') 
                
                
            except ChatRoom.DoesNotExist :
                friend.last_message_added = None
            
        else :
            friend.unread_msg = ChatRoom.objects.filter(receiver = user,sender=friend.following, unread_messages=False).count()
            
            try :
                friend.last_message_added =  ChatRoom.objects.filter(Q(sender=friend.following, receiver=user)|Q(sender=user, receiver=friend.following)).latest('timestamp')
                
            except ChatRoom.DoesNotExist :
                friend.last_message_added = None       
       
    return render(request,"chats/chat.html",{'friends':friends})
    
    
def chat_detail(request, username ):
    user = request.user
    friend = User.objects.get(username = username)
    
    messages = ChatRoom.objects.filter(Q(sender=friend, receiver=user)|Q(sender=user, receiver=friend)).order_by("timestamp")
    message_readed = ChatRoom.objects.filter(receiver = user,sender=friend, unread_messages=False).update(unread_messages=True)
    
   
    return render(request,"chats/chat_detail.html", {'friend':friend, 'messages':messages})


