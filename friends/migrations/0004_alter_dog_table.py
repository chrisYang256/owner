# Generated by Django 3.2.7 on 2021-09-14 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_alter_owner_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dog',
            table='dogs',
        ),
    ]
