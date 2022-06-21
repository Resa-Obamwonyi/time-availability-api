from rest_framework import viewsets
from rest_framework import permissions
from serializers import TimeSlotSerializer
from models import TimeSlots


class TimeSlotsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that receives the array of time hashes and handles the data appropriately.
    """
    serializer_class = TimeSlots
