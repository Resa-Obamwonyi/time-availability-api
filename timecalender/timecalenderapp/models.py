from django.db import models

# Model to help serialize incoming data
class TimeSlots(models.Model):
    from_time = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
