from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Friend 
from chats.models import ChatRoom

from accounts.models import Profile
from django.db.models import Q
# Create your views here.
# '''
@login_required
def notification(request):
    user = request.user
    followers = Friend.objects.filter(following=user, is_accepted=False).order_by('-created_at')
    
    return render(request, "friends/notification.html", {'followers': followers})
    
    
@login_required    
def search_friend(request):
    friends = Profile.objects.all().exclude(user = request.user)
    accepted_friends = Friend.objects.all()
    accepted_friend_ids = set()
    
    for relationship in accepted_friends:
        if relationship.follower == request.user and not relationship.is_accepted:
            accepted_friend_ids.add(relationship.following.id)
            
        if relationship.is_accepted and (relationship.follower == request.user or relationship.following == request.user ):
            accepted_friend_ids.add(relationship.follower.id)
            accepted_friend_ids.add(relationship.following.id)
    
    if request.method == "GET":
        search = request.GET.get("q")
        
        if search :
            if Profile.objects.filter(user__username__icontains = search).exists() :
                friends = Profile.objects.filter(user__username__icontains = search).exclude(user = request.user)
   
    return render(request, "friends/search.html", {'friends':friends, 'accepted_friends':accepted_friend_ids})


def follow(request,username):
    follower = request.user
    following = User.objects.get(username=username)
    friend,created = Friend.objects.get_or_create(follower=follower, following=following)
    friend.save()
    
    return redirect("friends:search")

    
def unfollow(request,username):
    user = request.user
    friend = User.objects.get(username = username)
    unfollow_friend = Friend.objects.filter(Q(follower=friend,following=user )|Q(follower=user,following=friend ))
    unfollow_friend.delete()
    messages = ChatRoom.objects.filter(Q(sender=friend, receiver=user)|Q(sender=user, receiver=friend))
    messages.delete()
    
    return redirect("friends:search")

def accept_follower(request,username):
    user = request.user
    accepted_follower = Friend.objects.filter(follower__username=username, following=user).update(is_accepted=True)
    
    return redirect("friends:notification")
    
def remove_follower(request, username):
    user = request.user
    removed_follower = Friend.objects.filter(follower__username=username, following=user)
    removed_follower.delete()
    
    return redirect("friends:notification")
    
