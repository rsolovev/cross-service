# Generated by Django 2.0.1 on 2019-03-22 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crossservice', '0002_auto_20190322_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='second_nmae',
            new_name='second_name',
        ),
    ]