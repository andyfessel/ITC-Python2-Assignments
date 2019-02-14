from django.db import models
from django.contrib.auth.models import User

#create models
#producttype, product, review

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)


    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    ##meetminid=models.CharField(max_length=255)
    ##meetminname=models.CharField(max_length=255)
    meetingminutesid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING) 
    ##meetmincreatedate=models.DateTimeField('Last Updated')
    ##meetminpublishdate=models.DateTimeField('Last Published')
    meetminattendance=models.ManyToManyField(User)
    meetmintext=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.meetingminutesid)

    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resname=models.CharField(max_length=255)
    restype=models.CharField(max_length=255)
    resurl=models.URLField(null=True, blank=True)
    resdateenter=models.DateField()
    resuser=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resdescription=models.CharField(max_length=255)
   

    def __str__(self):
        return str(self.resname)

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255)
    eventuserid=models.ManyToManyField(User)
    
    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'
    


