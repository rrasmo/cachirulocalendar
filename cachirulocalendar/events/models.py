from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    url = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    url = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pub_date = models.DateTimeField(null=True)
    place = models.CharField(max_length=200, null=True)
    community = models.ForeignKey(Community)

    def __unicode__(self):
        return self.name

