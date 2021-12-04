# Generated by Django 3.2.8 on 2021-11-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_voting', '0006_auto_20211107_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='real_participants',
        ),
        migrations.AddField(
            model_name='poll',
            name='absent_face_participants',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='absent_remote_participants',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='remote_participant',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
