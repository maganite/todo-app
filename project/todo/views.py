from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.exceptions import ValidationError
from datetime import datetime
from pytz import timezone

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

    def get(self,request, *args, **kwargs):
        # print(request.data)
        print(kwargs)
        valid_object = self.check(kwargs["pk"])
        serializer = TodoSerializers(valid_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def patch(self, request, pk):
        print(pk)
        valid_object = self.check(pk)
        print("hello")
        serializer = TodoSerializers(valid_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        valid_object = self.check(pk)
        valid_object.delete()
        return Response(status=status.HTTP_200_OK)
    
class ReminderView(APIView):
    def get(self, request, *args, **kwargs):
        queryset=Todo.objects.filter(id=kwargs["pk"])
        if queryset.exists():
            obj=queryset.first()
            serialized_data=TodoSerializers(obj)
            if(serialized_data.data['reminder_time'] is not None):
                #finding current time in datetime class and in string format using strftime() function
                now=datetime.now(timezone("Asia/Kolkata"))
                current_time_string=now.strftime("%Y-%m-%d %H:%M:%S")

                #calculating the time left for reminder but converting the string of reminder_time from model into datetime class
                remind_time = datetime.fromisoformat(serialized_data.data["reminder_time"])
                if(remind_time > now):
                    time_left = remind_time-now
                    req_data={"id": serialized_data.data["id"],
                            "current_time": current_time_string,
                            "reminder_time": serialized_data.data["reminder_time"],
                            "time_left for reminder": str(time_left),
                            }
                    return Response(req_data, status.HTTP_200_OK)
                else:
                    return Response({"message":"The reminder is already completed"})
            else:
                return Response({"message":"There is no reminder has been set for this todo"})
        else:
            return Response({"message":"the reminder for this todo is already done"})

        
