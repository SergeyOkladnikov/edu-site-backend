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
        question_pk = text_data_json['question_pk']
        question_text = text_data_json['question_text']
        question_number = text_data_json['question_number']
        chosen_answers = text_data_json['chosen_answers']
        is_correct = True
        connection_code = self.room_name
        print(text_data_json)
        for a in get_object_or_404(Question, pk=question_pk).answers.all():
            if a.pk in chosen_answers and not a.is_correct:
                is_correct = False
                break
            if a.pk not in chosen_answers and a.is_correct:
                is_correct = False
                break
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'answer_data',
                'name': name,
                'question_pk': question_pk,
                'question_text': question_text,
                'question_number': question_number,
                'is_correct': is_correct
            }
        )

    def answer_data(self, event):
        name = event['name']
        question_pk = event['question_pk']
        question_text = event['question_text']
        question_number = event['question_number']
        is_correct = event['is_correct']
        self.send(text_data=json.dumps({
            'name': name,
            'question_pk': question_pk,
            'question_text': question_text,
            'question_number': question_number,
            'is_correct': is_correct
        }))