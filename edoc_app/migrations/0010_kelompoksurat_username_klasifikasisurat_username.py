# Generated by Django 4.2.4 on 2023-10-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edoc_app', '0009_databasesurat_tahun'),
    ]

    operations = [
        migrations.AddField(
            model_name='kelompoksurat',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='klasifikasisurat',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
