# Generated by Django 2.0.5 on 2018-05-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CableSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cable_mark', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('cross_section', models.FloatField()),
            ],
        ),
    ]
