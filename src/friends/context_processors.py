from .models import Friend
from chats.models import ChatRoom

# Notifications
def notifications_length(request):
    user = request.user
    if user.is_authenticated:
        
        notifications_count = Friend.objects.filter(following=user, is_accepted=False).count()
        
    else:
        notifications_count = 0

    return {
        'notifications_length': notifications_count,
    }

# Meassages
def messages_length(request):
    user = request.user
    if user.is_authenticated:
        messages_count = ChatRoom.objects.filter(receiver = user , unread_messages=False).count()
    else:
        messages_count = 0

    return {'messages_length':messages_count}