# Generated by Django 3.2.4 on 2023-05-31 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_category_maincategoryname'),
    ]

    operations = [
        migrations.CreateModel(
            name='healthNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]