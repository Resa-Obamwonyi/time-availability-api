from .models import TimeSlots
from rest_framework import serializers


# serializer that uses model to clean up incoming data
class TimeSlotSerializer(serializers.Serializer):
    class Meta:
        model = TimeSlots
        fields = ["from_time", "to", "country_code"]
