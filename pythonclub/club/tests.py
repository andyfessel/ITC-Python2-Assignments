from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource
## from .forms import ProductForm, ReviewForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
# model tests

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Weekly Review')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        meetingminutes=MeetingMinutes(meetmintext='good meeting')
        self.assertEqual(str(meetingminutes), meetingminutes.meetmintext)

    def test_tablename(self):
        self.assertEqual(str(meetingminutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resname='Lenovo Laptop')
        self.assertEqual(str(resource), resource.resname)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class TestIndex(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')

class TestGetMeeting(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/meetinghistory')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingtitle'))
        self.assertEqual(response.status_code, 200)
        
    def tpyest_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingtitle'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/meetinghistory.html')

class New_Product_Form_Test(TestCase):

    ##imported from github/Steve - need to check for correct titles 02-25-19 12Noon

    # Valid Form Data
    def test_productForm_is_valid(self):
        form = ProductForm(data={'productname': "Surface", 'techtype': "laptop", 'user': "steve", 'entrydate': "2018-12-17", 'productURL':"http:microsoft.com", 'productdescription':"lightweight laptop" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = ProductForm(data={'productname': "Surface", 'techtype': "laptop", 'user': "steve", 'entrydate': "2018-12-17", 'productURL':"http:microsoft.com", 'productdescription':"lightweight laptop" })
        self.assertFalse(form.is_valid())

class TestLogInMessage(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/loginmessage.html')

class TestLogOutMessage(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/logoutmessage.html')

class TestMeetingID(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingid'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingid'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/meetingid.html')

class TestResourceType(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('restype'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('restype'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/type.html')

class TestMeetingTitle(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingtitle'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingtitle'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/meetinghistory.html')

class TestNewResource(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('newResource'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('newResource'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/resourceform.html')
