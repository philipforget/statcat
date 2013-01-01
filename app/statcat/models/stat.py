import datetime

from django.db import models



class Stat(models.Model):
    """The base unit of StatCat, stores one measurement.

    Each Stat is associated with the instrument from which it was measured as
    well as the date and time it was measured which may be different from the
    time this object was actually created. Keeping track of both date and
    timestamps gives us an idea on the latency which might exist in the system,
    intended or not.
    """
    instrument = models.ForeignKey('statcat.Instrument')
    # When this measurement was taken, may or may not be sent by instrument
    datestamp = models.DateTimeField(default=datetime.datetime.now, blank=True)
    # When we created this entry in the DB
    created = models.DateTimeField(auto_add_now=True)
