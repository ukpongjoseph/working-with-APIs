from rest_framework import serializers
from .models import Link
from dataclasses import field

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"