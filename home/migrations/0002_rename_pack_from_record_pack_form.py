# Generated by Django 4.0.6 on 2022-09-19 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='pack_from',
            new_name='pack_form',
        ),
    ]
