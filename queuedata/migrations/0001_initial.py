# Generated by Django 2.1.3 on 2018-11-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_number', models.IntegerField()),
                ('lab_name', models.TextField()),
            ],
        ),
    ]
