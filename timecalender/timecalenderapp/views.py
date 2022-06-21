from rest_framework import viewsets
from rest_framework import permissions
from serializers import TimeSlotSerializer
# from models import TimeSlots
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class TimeSlotsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that receives the array of time hashes and handles the data appropriately.
    """
    serializer_class = TimeSlotSerializer


    @action(detail=True, methods=['post'])
    def process_overlapping_time(self, request, pk=None):
        time_array_data = request.data
        return time_array_data
