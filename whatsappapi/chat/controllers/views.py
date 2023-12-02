from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.views import APIView
from ..services.tasks import enter_chatroom, leave_chatroom
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

from .serializers import UserSerializer
from ..entities.models import ChatRoom
from .serializers import ChatRoomSerializer, MessageSerializer

class ListChatRoom(generics.ListAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class CreateChatRoom(generics.CreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(views.APIView):
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(UserSerializer(user).data)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(views.APIView):
    authentication_classes = []
    def post(self, request):
        logout(request)
        return Response({"success": "Successfully logged out."})


@api_view(['POST'])
def enter_chatroom_view(request):
    user_id = request.data.get('user_id')
    room_id = request.data.get('room_id')

    if user_id is None or room_id is None:
        return Response({'error': 'Missing user_id or room_id'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        room = ChatRoom.objects.get(id=room_id)
    except ChatRoom.DoesNotExist:
        return Response({'error': 'Chatroom not found'}, status=status.HTTP_404_NOT_FOUND)


    enter_chatroom.delay(user_id, room_id)
    return Response({'status': 'Entering chatroom initiated'}, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def leave_chatroom_view(request):
    user_id = request.data.get('user_id')
    room_id = request.data.get('room_id')

    if user_id is None or room_id is None:
        return Response({'error': 'Missing user_id or room_id'}, status=status.HTTP_400_BAD_REQUEST)
    
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        room = ChatRoom.objects.get(id=room_id)
    except ChatRoom.DoesNotExist:
        return Response({'error': 'Chatroom not found'}, status=status.HTTP_404_NOT_FOUND)

    leave_chatroom.delay(user_id, room_id)
    return Response({'status': 'Leaving chatroom initiated'}, status=status.HTTP_202_ACCEPTED)


class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)