# Generated by Django 4.0.1 on 2022-01-18 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_location_meetups_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetups',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.Participant'),
        ),
    ]
