from abc import ABC, abstractmethod
from rest_framework.response import Response
from . import serializers
from rest_framework import status


class AbstractStrategy(ABC):

    @abstractmethod
    def createSerializer(self, request, context_id) -> Response:
        pass


class ContextStrategy:

    def __init__(self):
        self.strategy = None

    def setStrategy(self, strategy=None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = DefaultStrategy()

    def executeStrategy(self, request, context_id):
        result = self.strategy.createSerializer(request, context_id)
        return result


class FirstClassSubject(AbstractStrategy):

    def createSerializer(self, request, context_id) -> Response:  # The first creation method
        request.data["name"] = request.data["name"] + "0"

        serializer = serializers.SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecondClassSubject(AbstractStrategy):

    def createSerializer(self, request, context_id) -> Response: # The second creation method
        request.data["name"] = request.data["name"] + "1"

        serializer = serializers.SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DefaultStrategy(AbstractStrategy):

    def createSerializer(self, request, context_id) -> Response: # Default creation method
        request.data["name"] = request.data["name"] + "2"

        serializer = serializers.SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(context_id=context_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)