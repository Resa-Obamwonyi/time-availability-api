from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import convert_to_utc, get_overlapping_time


class TimeSlotsApi(APIView):
    """
    API view that receives the array of time hashes and handles the data appropriately.
    """

    permission_classes = [AllowAny]

    # post request endpoint
    def post(self, request):
        # incoming request data
        time_array_data = request.data.get("time_slots")
        if not time_array_data:
            return Response(
                dict(error="invalid time slot data provided"),
                status=status.HTTP_400_BAD_REQUEST,
            )

        # initialize empty array to store utc conversions
        utc_time_array = []
        for time_slot in time_array_data:
            utc_resp = convert_to_utc(time_slot)
            if type(utc_resp) == list:
                utc_time_array.append(utc_resp)
            else:
                return Response(
                    dict(error=utc_resp), status=status.HTTP_424_FAILED_DEPENDENCY
                )

        # If "None" appears in array, there is no need to confirm overlapping time
        if None in utc_time_array:
            return Response(
                dict(error="Sorry, there are no overlapping time slots available"),
                status=status.HTTP_424_FAILED_DEPENDENCY,
            )

        # otherwise send all converted time array to a util to get the over lapping time
        overlapping_time = get_overlapping_time(utc_time_array)

        # return over lapping time or an error message
        if overlapping_time:
            return Response(dict(response=overlapping_time), status=status.HTTP_200_OK)

        return Response(
            dict(error="Sorry, there are no overlapping time slots available"),
            status=status.HTTP_424_FAILED_DEPENDENCY,
        )
