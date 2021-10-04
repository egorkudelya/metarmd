from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os


class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Context
        fields = ['id', 'name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ['id', 'name']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    # events = serializers.SerializerMethodField()
    events = EventSerializer(many=True)

    class Meta:
        model = models.User
        fields = ['id', 'name', 'events']

    def get_events(self, user_instance):
        qset = models.PersonalizedEvent.objects.filter(user=user_instance)
        a = [ev for ev in qset]
        events = []
        for cl in a:
            events.append(cl.event)
        return [EventSerializer(ev).data for ev in events]
        # return [PersonalizedEventSerializer(ev).data for ev in qset]

class PersonalizedEventSerializer(serializers.ModelSerializer):
    # create_pe = serializers.SerializerMethodField()

    class Meta:
        model = models.PersonalizedEvent
        fields = '__all__'


    # def get_create_pe(self, validated_data):
    #     try:
    #         id = validated_data['context_id']
    #     except Exception:
    #         return
    #     users = models.User.objects.filter(context__id=id)
    #     event = models.Event.objects.filter(id=validated_data['event_id'])
    #
    #     for user in users:
    #         models.PersonalizedEvent.objects.create(event=event[0], user=user)
    #     return
