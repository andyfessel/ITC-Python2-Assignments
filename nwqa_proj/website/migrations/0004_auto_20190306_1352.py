# Generated by Django 2.1.4 on 2019-03-06 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190306_1345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommunityEvents',
            new_name='Celebrations',
        ),
        migrations.RenameField(
            model_name='celebrations',
            old_name='communityevents_attendees',
            new_name='celebrations_attendees',
        ),
        migrations.RenameField(
            model_name='celebrations',
            old_name='communityevents_eventdate',
            new_name='celebrations_eventdate',
        ),
        migrations.RenameField(
            model_name='celebrations',
            old_name='communityevents_events',
            new_name='celebrations_events',
        ),
        migrations.RenameField(
            model_name='celebrations',
            old_name='communityevents_resources',
            new_name='celebrations_resources',
        ),
        migrations.RenameField(
            model_name='celebrations',
            old_name='communityevents_volunteers',
            new_name='celebrations_volunteers',
        ),
        migrations.AlterModelTable(
            name='celebrations',
            table='celebrations',
        ),
    ]
