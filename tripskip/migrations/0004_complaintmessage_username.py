# Generated by Django 3.1.2 on 2020-10-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripskip', '0003_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintmessage',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
