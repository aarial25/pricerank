# Generated by Django 4.0.6 on 2022-09-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_pack_from_record_pack_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='volume_l15',
            new_name='sum_of_non_meo',
        ),
        migrations.AddField(
            model_name='record',
            name='volume_L15',
            field=models.CharField(default='-', max_length=100),
        ),
    ]