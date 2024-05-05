import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

        # Add the user to a specific chat room (e.g., based on URL parameters)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Add the user to the chat room's group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Send a message to the WebSocket client to confirm the connection
        await self.send(json.dumps({'message': 'Connected to the chat room.'}))

    async def disconnect(self, close_code):
        # Remove the user from the chat room's group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming messages from the WebSocket client
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Broadcast the message to all users in the chat room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send the chat message to the WebSocket client
        message = event['message']

        await self.send(json.dumps({'message': message}))
