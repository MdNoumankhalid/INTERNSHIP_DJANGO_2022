# Generated by Django 3.0 on 2022-09-20 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intership_app', '0002_auto_20220919_1221'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerOrder',
            new_name='MyOrder',
        ),
    ]