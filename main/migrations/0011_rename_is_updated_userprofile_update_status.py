# Generated by Django 4.2.3 on 2024-02-04 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_userprofile_is_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_updated',
            new_name='update_status',
        ),
    ]
