from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TimeSlotSerializer
from .models import TimeSlots
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TimeSlotsApi(APIView):
    """
    API endpoint that receives the array of time hashes and handles the data appropriately.
    """
    permission_classes = [AllowAny]


    def post(self, request):
        time_array_data = request.data
        return time_array_data
