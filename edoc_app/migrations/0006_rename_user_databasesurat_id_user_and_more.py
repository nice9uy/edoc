# Generated by Django 4.2.4 on 2023-09-06 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edoc_app', '0005_rename_surat_namasurat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='databasesurat',
            old_name='user',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='kelompoksurat',
            old_name='username',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='klasifikasisurat',
            old_name='username',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='namasurat',
            old_name='nama_Surat',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='namasurat',
            old_name='username',
            new_name='nama_surat',
        ),
    ]
