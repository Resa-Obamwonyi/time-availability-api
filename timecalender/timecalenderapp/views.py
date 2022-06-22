from .serializers import TimeSlotSerializer
from .models import TimeSlots
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import convert_to_utc

class TimeSlotsApi(APIView):
    """
    API view that receives the array of time hashes and handles the data appropriately.
    """
    permission_classes = [AllowAny]

    # post request endpoint
    def post(self, request):
        # incoming request data
        time_array_data = request.data.get('time_slots')
        if not time_array_data:
            return Response(dict(error="invalid time slot data provided"), status=status.HTTP_400_BAD_REQUEST)
        # initialize empty array to store gmt conversions
        gmt_time_array = []
        for time_slot in time_array_data:
            gmt_time = convert_to_utc(time_slot)
            gmt_time_array.append(gmt_time)

        return Response(dict(response=gmt_time_array), status=status.HTTP_200_OK)
