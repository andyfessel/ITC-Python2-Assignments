# Generated by Django 2.1.4 on 2019-01-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_meetingminutes_meetmintext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingminutes',
            name='meetmintext',
            field=models.TextField(blank=True),
        ),
    ]