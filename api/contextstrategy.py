from abc import ABC, abstractmethod
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Context, User, Event, Subject, PersonalizedEvent
from django.http import Http404
from rest_framework import status
import requests


class AbstractStrategy(ABC):

    def _modify(self, data):
        pass

    @abstractmethod
    def createSerializer(self, request, context_id) -> Response:
        pass


class ContextStrategy:

    def __init__(self):
        self.strategy = None

    def setStrategy(self, strategy) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = DefaultStrategy()

    def executeStrategy(self, request, context_id):
        result = self.strategy.createSerializer(request, context_id)
        return result


class FirstClassSubject(AbstractStrategy):

    def _modify(self, data):
        data["name"] = data["name"] + "0"
        return data

    def createSerializer(self, request, context_id) -> Response:
        data = self._modify(request.data)

        serializer = serializers.SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecondClassSubject(AbstractStrategy):

    def _modify(self, data):
        data["name"] = data["name"] + "1"
        return data

    def createSerializer(self, request, context_id) -> Response:
        data = self._modify(request.data)

        serializer = serializers.SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DefaultStrategy(AbstractStrategy):

    def _modify(self, data):
        return data

    def createSerializer(self, request, context_id) -> Response:
        data = self._modify(request.data)

        serializer = serializers.SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)