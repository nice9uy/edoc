# Generated by Django 4.2.4 on 2023-08-31 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edoc_app', '0002_kelompoksurat_delete_jenissurat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelompoksurat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='klasifikasisurat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]