# Generated by Django 4.2.6 on 2023-10-08 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_djanghoteluser_roomcost_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomcost',
            old_name='room_number',
            new_name='room',
        ),
    ]
