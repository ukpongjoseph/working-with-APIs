from django.shortcuts import render
from rest_framework import viewsets
from links.serializers import LinkSerializer
from .models import Link
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import GenericAPIView
import rest_framework.generics
from I4G011873VT1.links import serializers
from I4G011873VT1.links.serializers import LinkSerializer

# Create your views here.

class PostListApi(generic.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(generic.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(generic.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(generic.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(generic.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer