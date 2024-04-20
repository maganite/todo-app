from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.exceptions import ValidationError
# Create your views here.

class TodoListAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()

    def post(self, request):
        serializers = self.get_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            full_data = TodoSerializers(Todo.objects.all(), many=True)
            return Response(full_data.data, status=status.HTTP_201_CREATED)



class TodoAPIView(APIView):
    def check(self, pk):
        try:
            obj = Todo.objects.get(id=pk)
            serializer = TodoSerializers(obj)
            return obj
        except Exception as e:
            print("the id doesnot exist")
            raise ValidationError(e)

    def get(self,request, pk):
        valid_object = self.check(pk)
        serializer = TodoSerializers(valid_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def patch(self, request, pk):
        valid_object = self.check(pk)
        serializer = TodoSerializers(valid_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        valid_object = self.check(pk)
        valid_object.delete()
        return Response(status=status.HTTP_200_OK)
