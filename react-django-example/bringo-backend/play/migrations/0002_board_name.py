# Generated by Django 3.0.1 on 2019-12-19 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='name',
            field=models.CharField(default='blank', max_length=255),
            preserve_default=False,
        ),
    ]