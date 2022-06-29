from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# Test Time slot api Endpoint
class TestTimeSlotApi(APITestCase):
    def setUp(self):
        self.data = {
            "time_slots": [
                {
                    "from": "2022-05-04T09: 00: 00.0-05: 00",
                    "to": "2022-05-04T21: 00: 00.0-05: 00",
                    "CC": "US",
                },
                {
                    "from": "2022-05-04T10: 00: 00.0+01: 00",
                    "to": "2022-05-04T12: 00: 00.0+01: 00",
                    "CC": "NG",
                },
                {
                    "from": "2022-05-04T11: 00: 00.0+05: 30",
                    "to": "2022-05-04T19: 00: 00.0+05: 30",
                    "CC": "IN",
                },
            ]
        }

        self.holiday_data = {
            "time_slots": [
                {
                    "from": "2022-05-02T09: 00: 00.0+08: 00",
                    "to": "2022-05-02T17: 00: 00.0+08: 00",
                    "CC": "SG",
                },
                {
                    "from": "2022-05-02T09: 00: 00.0+01: 00",
                    "to": "2022-05-02T17: 00: 00.0+01: 00",
                    "CC": "NG",
                },
                {
                    "from": "2022-05-02T09: 00: 00.0+05: 30",
                    "to": "2022-05-02T17: 00: 00.0+05: 30",
                    "CC": "IN",
                },
            ]
        }

        self.weekend_data = {
            "time_slots": [
                {
                    "from": "2022-06-26T09: 00: 00.0+08: 00",
                    "to": "2022-06-26T17: 00: 00.0+08: 00",
                    "CC": "SG",
                },
                {
                    "from": "2022-06-26T09: 00: 00.0+01: 00",
                    "to": "2022-06-26T17: 00: 00.0+01: 00",
                    "CC": "NG",
                },
                {
                    "from": "2022-06-26T09: 00: 00.0+05: 30",
                    "to": "2022-06-26T17: 00: 00.0+05: 30",
                    "CC": "IN",
                },
            ]
        }

    def test_get_correct_overlapping_schedule(self):
        url = reverse("timeslot")
        response = self.client.post(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "response": [
                    {"from": "2022-05-04T09:00:00Z", "to": "2022-05-04T11:00:00Z"}
                ]
            },
        )

    def test_get_overlapping_schedule_holiday(self):
        url = reverse("timeslot")
        response = self.client.post(url, self.holiday_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_424_FAILED_DEPENDENCY)
        self.assertEqual(response.json(), {"error": "It's a holiday in Asia/Singapore"})

    def test_get_overlapping_schedule_weekend(self):
        url = reverse("timeslot")
        response = self.client.post(url, self.weekend_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_424_FAILED_DEPENDENCY)
        self.assertEqual(response.json(), {"error": "It's a weekend in Asia/Singapore"})
