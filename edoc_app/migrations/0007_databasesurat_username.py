# Generated by Django 4.2.4 on 2023-09-19 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edoc_app', '0006_rename_user_databasesurat_id_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='databasesurat',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
