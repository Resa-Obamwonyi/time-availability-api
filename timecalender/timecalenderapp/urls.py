from django.urls import path
from .views import TimeSlotsApi

urlpatterns = [
    path("timeslot", TimeSlotsApi.as_view(), name="timeslot"),
]
