# Generated by Django 4.2.6 on 2023-10-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('keyword', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('resp', models.CharField(max_length=500)),
            ],
        ),
    ]