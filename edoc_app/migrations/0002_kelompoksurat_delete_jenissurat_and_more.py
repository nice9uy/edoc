# Generated by Django 4.2.4 on 2023-08-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edoc_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KelompokSurat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('kode', models.CharField(max_length=10)),
                ('nama_kelompok', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'KelompokSurat',
            },
        ),
        migrations.DeleteModel(
            name='JenisSurat',
        ),
        migrations.RenameField(
            model_name='databasesurat',
            old_name='katagori',
            new_name='kelompok',
        ),
        migrations.AlterField(
            model_name='klasifikasisurat',
            name='kode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='klasifikasisurat',
            name='nama_klasifikasi',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='klasifikasisurat',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
