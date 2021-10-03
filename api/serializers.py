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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'name']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = ['name', 'id']


class PersonalizedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PersonalizedEvent
        fields = ['id', 'is_completed', 'user']
