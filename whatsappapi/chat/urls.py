from django.urls import path,include, re_path
from . import views
from .views import LoginView, LogoutView, FileUploadView
from .consumers import ChatConsumer


urlpatterns = [
    path('chatrooms/', views.ListChatRoom.as_view(), name='list-chatrooms'),
    path('create_chatroom/', views.CreateChatRoom.as_view(), name='create-chatroom'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    
    path('enter/', views.enter_chatroom_view, name='enter-chatroom'),
    path('leave/', views.leave_chatroom_view, name='leave-chatroom'),

    path('upload/', FileUploadView.as_view(), name='file-upload'),

]

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\w+)/$', ChatConsumer.as_asgi()),
]
