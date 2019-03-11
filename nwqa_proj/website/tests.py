from django.test import TestCase
from .models import HomeOwner, Project, Traffic, Safety, NeedGoodNeighbor, BeGoodNeighbor, Emergency, Celebrations
from .forms import ProjectForm
from datetime import datetime
from django.urls import reverse

class HomeOwnerTest(TestCase):
    def test_stringOutput(self):
        homeowner=HomeOwner(namelast='Smith')
        self.assertEqual(str(homeowner), homeowner.namelast)

    def test_tablename(self):
        self.assertEqual(str(HomeOwner._meta.db_table), 'homeowner')

class ProjectTest(TestCase):
    def test_stringOutput(self):
        project=Project(projectname='Safety Plan')
        self.assertEqual(str(project), project.projectname)

    def test_tablename(self):
        self.assertEqual(str(Project._meta.db_table), 'projectname')

class TrafficTest(TestCase):
    def test_stringOutput(self):
        traffic=Traffic(traffic_type='Speeding')
        self.assertEqual(str(traffic), traffic.traffic_type)

    def test_tablename(self):
        self.assertEqual(str(Traffic._meta.db_table), 'traffic_type')

class NewProjectFormTest(TestCase):
    def test_projectForm_is_valid(self):
        form = ProjectForm(data={'projectname': "Street Cleaning", 'projecttype': "environment", 'projectresources': "garden tools", 'productdescription': "saturday work party", 'projectcreated_date': "2019-4-10"})
        self.assertTrue(form.is_valid())

    def test_projectForm_invalid(self):
        form = ProjectForm(data={'projectname': "12345", 'projecttype': "environment", 'projectresources': "garden tools", 'productdescription': "saturday work party", 'projectcreated_date': "2019-4-10"})
        self.assertFalse(form.is_valid())

class TestLogInMessage(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/loginmessage.html')

class TestLogOutMessage(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/logoutmessage.html')

