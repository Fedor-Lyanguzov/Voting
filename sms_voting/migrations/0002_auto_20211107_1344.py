# Generated by Django 3.2.8 on 2021-11-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_voting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='no_votes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='real_participants',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='yes_votes',
            field=models.IntegerField(null=True),
        ),
    ]