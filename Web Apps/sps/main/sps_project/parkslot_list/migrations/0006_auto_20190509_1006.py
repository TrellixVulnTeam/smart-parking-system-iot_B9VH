# Generated by Django 2.1.7 on 2019-05-09 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkslot_list', '0005_auto_20190509_0920'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='HistorySlot',
        ),
    ]