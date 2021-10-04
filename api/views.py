from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Context, User, Event, Subject, PersonalizedEvent
from django.http import Http404
from rest_framework import status


class ContextView(APIView):

    def get(self, request):
        contexts = Context.objects.all()
        serializer = serializers.ContextSerializer(contexts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ContextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectView(APIView):

    def get(self, request, context_id):
        subjects = Subject.objects.filter(context__id=context_id)
        serializer = serializers.SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request, context_id):
        try:
            Context.objects.get(pk=context_id)
        except Context.DoesNotExist:
            raise Http404

        serializer = serializers.SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    def get(self, request, context_id):
        users = User.objects.filter(context__id=context_id)
        serializer = serializers.SubjectSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, context_id):
        try:
            Context.objects.get(pk=context_id)
        except Context.DoesNotExist:
            raise Http404

        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventView(APIView):

    def get(self, request, **kwargs):
        subject_id = kwargs["subject_id"]
        events = Event.objects.filter(subject__id=subject_id)
        serializer = serializers.EventSerializer(events, many=True)
        return Response(serializer.data)


    def post(self, request,  **kwargs):
        subject_id = kwargs["subject_id"]
        try:
            Subject.objects.get(pk=subject_id)
        except Subject.DoesNotExist:
            raise Http404

        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            m = serializer.save(subject_id=subject_id)
            vd = {"context_id": kwargs['context_id'],
                  "event_id": m.id}
            personalized = serializers.PersonalizedEventSerializer.get_create_pe(self,validated_data=vd)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEventsView(APIView):

    def get(self, request, **kwargs):
        # print(kwargs)
        user_id = kwargs["user_id"]
        user = User.objects.filter(id=user_id)
        serializer = serializers.UserSerializer(user, many=True)
        return Response(serializer.data)