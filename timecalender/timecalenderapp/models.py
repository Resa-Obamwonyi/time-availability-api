from django.db import models

# Model to help serialize incoming data
class TimeSlots(models.Model):
    from_time = models.CharField()
    to = models.CharField()
    country_code = models.CharField()
