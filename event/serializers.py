from django.urls import reverse
from rest_framework import serializers
from event.models import * 

class DashboardSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Member
        fields = __all__
