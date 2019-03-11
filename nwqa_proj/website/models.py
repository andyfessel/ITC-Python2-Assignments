from django.db import models
from django.conf import settings
from django.utils import timezone

class HomeOwner(models.Model):
    namelast=models.CharField(max_length=255)
    namefirst=models.CharField(max_length=255)
    address_street=models.CharField(max_length=255)
    apartment_no=models.CharField(max_length=255)
    phone_no=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    member_status=models.CharField(max_length=255)
    memberupdate_date=models.DateTimeField(default=timezone.now)
    membersignup_date=models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.namelast

    class Meta:
        db_table='homeowner'

class Project(models.Model):
    projectname=models.CharField(max_length=255)
    projecttype=models.CharField(max_length=255)
    projectresources=models.CharField(max_length=255)
    productdescription=models.CharField(max_length=255)
    projectcreated_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.projectname

    class Meta:
        db_table='project'

class Traffic(models.Model):
    #traffic_issue=models.CharField(max_length=255)
    #traffic_issue_description=models.CharField(max_length=255)
    traffic_type=models.CharField(max_length=255)
    traffic_resources=models.CharField(max_length=255)
    traffic_events=models.CharField(max_length=255)
    traffic_volunteers=models.CharField(max_length=255)
    trafffic_attendees=models.CharField(max_length=255)
    traffic_events=models.CharField(max_length=255)
    traffic_eventdate=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.traffic_type

    class Meta:
        db_table='traffic'

class Safety(models.Model):
    #safety_issue=models.CharField(max_length=255)
    #safety_issue_descriptionCharField(max_length=255)
    safety_type=models.CharField(max_length=255)
    safety_resources=models.CharField(max_length=255)
    safety_events=models.CharField(max_length=255)
    safety_volunteers=models.CharField(max_length=255)
    safety_attendees=models.CharField(max_length=255)
    safety_events=models.CharField(max_length=255)
    safety_eventdate=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.safety_type

    class Meta:
        db_table='safety'

class NeedGoodNeighbor(models.Model):
    needgoodneighbor_issue=models.CharField(max_length=255)
    needgoodneighbor_resources=models.CharField(max_length=255)
    needgoodneighbor_events=models.CharField(max_length=255)
    needgoodneighbor_volunteers=models.CharField(max_length=255)
    needgoodneighbor_attendees=models.CharField(max_length=255)
    needgoodneighbor_events=models.CharField(max_length=255)
    needgoogneighbor_eventdate=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.needgoodneighbor_issue

    class Meta:
        db_table='needgoodneighbor'

class BeGoodNeighbor(models.Model):
    begoodneighbor_issue=models.CharField(max_length=255)
    begoodneighbor_resources=models.CharField(max_length=255)
    begoodneighbor_events=models.CharField(max_length=255)
    begoodneighbor_volunteers=models.CharField(max_length=255)
    begoodneighbor_attendees=models.CharField(max_length=255)
    begoodneighbor_events=models.CharField(max_length=255)
    begoogneighbor_eventdate=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.begoodneighbor_issue

    class Meta:
        db_table='begoodneighbor'

class Emergency(models.Model):
    emergency_issue=models.CharField(max_length=255)
    emergency_type=models.CharField(max_length=255)
    emergency_resources=models.CharField(max_length=255)
    emergency_events=models.CharField(max_length=255)
    emergency_volunteers=models.CharField(max_length=255)
    emergency_attendees=models.CharField(max_length=255)
    emergency_events=models.CharField(max_length=255)
    emergency_eventdate=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.emergency_issue

    class Meta:
        db_table='emergency'

class Celebrations(models.Model):
    celebrations_events=models.CharField(max_length=255)
    celebrations_resources=models.CharField(max_length=255)
    celebrations_volunteers=models.CharField(max_length=255)
    celebrations_attendees=models.CharField(max_length=255)
    celebrations_events=models.CharField(max_length=255)
    celebrations_eventdate=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.celebrations_events

    class Meta:
        db_table='celebrations'

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    