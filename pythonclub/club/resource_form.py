from django import forms
class ResourceForm(forms.Form):
    resname=forms.CharField(max_length=255,
        label='New Resource Input')
    restype=forms.CharField(max_length=255,
        label='Resource Type')
    resurl=forms.URLField(null=True, blank=True,
        label='Resource URL')
    resdateenter=forms.DateField(
        label='Date Resource Entered')
    resuser=forms.ForeignKey(User, on_delete=models.DO_NOTHING,
        label='User of Resource')
    resdescription=forms.CharField(max_length=255,
        label='Description of Resource')
    