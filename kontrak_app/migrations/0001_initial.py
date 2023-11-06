# Generated by Django 4.2.4 on 2023-11-06 07:16

from django.db import migrations, models
import kontrak_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontrak',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('id_user', models.CharField(max_length=4)),
                ('username', models.CharField(max_length=30)),
                ('no_kontrak', models.IntegerField()),
                ('sumber_dana', models.CharField(max_length=6)),
                ('tgl', models.DateField()),
                ('tentang', models.CharField(max_length=200)),
                ('upload_file', models.FileField(upload_to=kontrak_app.models.user_folder)),
                ('today', models.DateField()),
                ('tahun', models.CharField(max_length=4)),
            ],
        ),
    ]
