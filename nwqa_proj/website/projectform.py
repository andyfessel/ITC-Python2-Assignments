from django import forms
class ProjectForm(forms.Form):
    projectname=forms.CharField(max_length=255,
        label='New Project Input')
    projecttype=forms.CharField(max_length=255,
        label='Type of Project')
    projectresources=forms.CharField(max_length=255,
        label='Resources Required')
    productdescription=forms.CharField(max_length=255,
        label='Description of Project')
    projectcreated_date=forms.DateTimeField(label='Date Project Entered')
    
    
    