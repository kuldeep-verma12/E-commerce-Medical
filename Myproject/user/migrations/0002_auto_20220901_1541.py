# Generated by Django 3.2.4 on 2022-09-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contectus',
            old_name='Massage',
            new_name='Message',
        ),
        migrations.AlterField(
            model_name='contectus',
            name='Email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contectus',
            name='Mobile',
            field=models.CharField(max_length=40),
        ),
    ]
