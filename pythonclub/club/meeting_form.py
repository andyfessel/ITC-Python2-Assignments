from django import forms
class MeetingForm(forms.Form):
    meetingtitle=forms.CharField(max_length=255,
        label='New Meeting Title')
    meetingdate=forms.DateField(
        label='Date of Meeting')
    meetingtime=forms.DateField(
        label='Time of Meeting')
    meetinglocation=forms.DateField(
        label='Location of Meeting')
    meetingagenda=forms.CharField(max_length=255,
        label='User of Resource')
   
