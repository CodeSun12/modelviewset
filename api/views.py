from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

# TODO MODELVIEWSET TO DO ALL FUCNCTIONALITIES WITH SIMPLE CODE AND BASIC AUTHENTICATION IMPLEMENTATION

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]



# # TODO THIS CLASS IS COMBINATION OF LIST CLASS AND CREATE CLASS
# class LCStudentApi(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BaseAuthentication]
#     permission_classes = [IsAuthenticated]
#
#
# # TODO THIS CLASS IS COMBINATION OF ALL THE REMAINING CLASSES LIKE RETRIEVING, UPDATING AND DESTROYING
# class URDStudentApi(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer