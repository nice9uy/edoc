# Generated by Django 4.2.4 on 2023-09-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edoc_app', '0004_surat_remove_kelompoksurat_kode_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Surat',
            new_name='NamaSurat',
        ),
    ]
