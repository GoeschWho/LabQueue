# Generated by Django 2.1.3 on 2018-11-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.TextField()),
            ],
        ),
    ]
