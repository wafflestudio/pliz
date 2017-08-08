from django.shortcuts import render
from rest_framework import generics
from errands.serializers import ErrandSerializer
from errands.models import Errand
from rest_framework import permissions
from errands.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes



class Delivery(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset=Errand.objects.filter(category="DELIVERY")
    serializer_class= ErrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Homework(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset=Errand.objects.filter(category="HOMEWORK")
    serializer_class= ErrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Etc(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset= Errand.objects.filter(category="ETC")
    serializer_class= ErrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ErrandList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset=Errand.objects.all()
    serializer_class= ErrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ErrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Errand.objects.all()
    serializer_class= ErrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
