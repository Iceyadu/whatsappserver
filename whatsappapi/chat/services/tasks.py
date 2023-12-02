# chat/tasks.py

from celery import shared_task
from django.contrib.auth import get_user_model
from ..entities.models import ChatRoom

@shared_task
def enter_chatroom(user_id, room_name):
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
        room = ChatRoom.objects.get(name=room_name)
        room.users.add(user)
        room.save()
    except (User.DoesNotExist, ChatRoom.DoesNotExist):
        pass  # Handle the exception as appropriate

@shared_task
def leave_chatroom(user_id, room_id):
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
        room = ChatRoom.objects.get(id=room_id)
        room.users.remove(user)
        room.save()
    except (User.DoesNotExist, ChatRoom.DoesNotExist):
        pass  # Handle
