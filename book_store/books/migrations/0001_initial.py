# Generated by Django 4.2.7 on 2023-11-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pages', models.IntegerField(default=0)),
                ('rating', models.IntegerField(max_length=125)),
            ],
        ),
    ]
