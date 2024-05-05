from django.urls import path
from .views import ChatRoomListAPIView, MessageListAPIView

urlpatterns = [
    path('api/chat-rooms/', ChatRoomListAPIView.as_view(), name='chatroom-list'),
    path('api/messages/', MessageListAPIView.as_view(), name='message-list'),
]
