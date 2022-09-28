# Generated by Django 2.1.5 on 2019-04-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0005_addfir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addregister',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('name2', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('type1', models.CharField(max_length=100)),
                ('occ', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='register/')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]