import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from django.shortcuts import get_object_or_404

from .models import *

class QuizConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json['name']
        question = text_data_json['question']
        chosen_answers = text_data_json['chosen_answers']
        is_correct = True
        connection_code = self.room_name
        for a in chosen_answers:
            if not get_object_or_404(Question, pk=question).answers.get(pk=a).is_correct:
                is_correct = False
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'answer_data',
                'name': name,
                'question': question,
                'is_correct': is_correct
            }
        )

    def answer_data(self, event):
        name = event['name']
        question = event['question']
        is_correct = event['is_correct']
        self.send(text_data=json.dumps({
            'name': name,
            'question': question,
            'is_correct': is_correct
        }))