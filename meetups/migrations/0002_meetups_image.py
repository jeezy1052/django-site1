# Generated by Django 4.0.1 on 2022-01-17 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetups',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
