import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Responses


class ChatConsumer(WebsocketConsumer):
    
    def _find_keyword(self, phrase):
        if "booking" in phrase.lower():
            return Responses.objects.get(keyword = 'booking').resp
        if "representative" in phrase.lower():
            return Responses.objects.get(keyword = 'representative').resp
        if "hello" in phrase.lower():
            return Responses.objects.get(keyword = 'hello').resp
        if "thank you" in phrase.lower():
            return Responses.objects.get(keyword = 'thank you').resp
        

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket (from web page)
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        automod = text_data_json["automod"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "username": username, "automod": automod}
        )

    # Receive message from room group (to web page)
    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        automod = event["automod"]
        resp = self._find_keyword(message)
        reply = ''
        if(username != 'RealModerator' and automod == 'automodeon'):
            if(resp):
                reply = 'Automod' + ': ' + resp + '\n'
            else:
                reply = 'Automod' + ': ' + Responses.objects.get(keyword = 'responsenotfound').resp + '\n'
        if(username == 'RealModerator' and 'Automod' not in message):
            automod = 'automodeoff'
        if(username == 'RealModerator' and 'Automod' in message):
            automod = 'automodeon'
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": username + ': ' + message, 'reply': reply, 'automod': automod}))