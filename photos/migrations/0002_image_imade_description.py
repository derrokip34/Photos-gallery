# Generated by Django 3.0.6 on 2020-05-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imade_description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]