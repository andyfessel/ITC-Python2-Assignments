# Generated by Django 2.1.4 on 2019-02-13 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20190127_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meetingid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]