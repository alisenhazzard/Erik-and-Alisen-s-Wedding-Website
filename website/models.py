"""==========================================================================
models.py

Contains all our models (guestbook)

============================================================================="""
from django.db import models
from django.conf import settings

"""=============================================================================

Models

============================================================================="""
#----------------------------------------
#Guest book
#----------------------------------------
class GuestBook(models.Model):
    #Name is the submitter
    name = models.CharField(
        max_length=255
    )

    #Message is the message content they submit
    message = models.TextField()

    #Store the date the message was created.  Date is automatically generated
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s (on %s) - %s' % (self.name, self.message, self.date)
