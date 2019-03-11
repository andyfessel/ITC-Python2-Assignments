# Generated by Django 2.1.4 on 2019-03-06 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeGoodNeighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begoodneighbor_issue', models.CharField(max_length=255)),
                ('begoodneighbor_resources', models.CharField(max_length=255)),
                ('begoodneighbor_volunteers', models.CharField(max_length=255)),
                ('begoodneighbor_attendees', models.CharField(max_length=255)),
                ('begoodneighbor_events', models.CharField(max_length=255)),
                ('begoogneighbor_eventdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'begoodneighbor',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celebrations_resources', models.CharField(max_length=255)),
                ('celebrations_volunteers', models.CharField(max_length=255)),
                ('celebrations_attendees', models.CharField(max_length=255)),
                ('celebrations_events', models.CharField(max_length=255)),
                ('celebration_eventdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'celebrations',
            },
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_issue', models.CharField(max_length=255)),
                ('emergency_type', models.CharField(max_length=255)),
                ('emergency_resources', models.CharField(max_length=255)),
                ('emergency_volunteers', models.CharField(max_length=255)),
                ('emergency_attendees', models.CharField(max_length=255)),
                ('emergency_events', models.CharField(max_length=255)),
                ('emergency_eventdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'emergency',
            },
        ),
        migrations.CreateModel(
            name='HomeOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namelast', models.CharField(max_length=255)),
                ('namefirst', models.CharField(max_length=255)),
                ('address_street', models.CharField(max_length=255)),
                ('apartment_no', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('member_status', models.CharField(max_length=255)),
                ('memberupdate_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('membersignup_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'homeowner',
            },
        ),
        migrations.CreateModel(
            name='NeedGoodNeighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needgoodneighbor_issue', models.CharField(max_length=255)),
                ('needgoodneighbor_resources', models.CharField(max_length=255)),
                ('needgoodneighbor_volunteers', models.CharField(max_length=255)),
                ('needgoodneighbor_attendees', models.CharField(max_length=255)),
                ('needgoodneighbor_events', models.CharField(max_length=255)),
                ('needgoogneighbor_eventdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'needgoodneighbor',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=255)),
                ('projecttype', models.CharField(max_length=255)),
                ('projectresources', models.CharField(max_length=255)),
                ('productdescription', models.CharField(max_length=255)),
                ('projectcreated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Safety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_type', models.CharField(max_length=255)),
                ('safety_resources', models.CharField(max_length=255)),
                ('safety_volunteers', models.CharField(max_length=255)),
                ('safety_attendees', models.CharField(max_length=255)),
                ('safety_events', models.CharField(max_length=255)),
                ('safety_eventdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'safety',
            },
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traffic_type', models.CharField(max_length=255)),
                ('traffic_resources', models.CharField(max_length=255)),
                ('traffic_volunteers', models.CharField(max_length=255)),
                ('trafffic_attendees', models.CharField(max_length=255)),
                ('traffic_events', models.CharField(max_length=255)),
                ('traffic_eventdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'traffic',
            },
        ),
    ]