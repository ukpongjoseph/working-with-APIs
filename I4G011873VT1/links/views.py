from django.shortcuts import render
from rest_framework import generics
from links.serializers import LinkSerializer
from rest_framework.generics import ListAPIView,CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView 
#from I4G011873VT1.links import serializers
#from I4G011873VT1.links.serializers import LinkSerializer
from .models import Link

# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
