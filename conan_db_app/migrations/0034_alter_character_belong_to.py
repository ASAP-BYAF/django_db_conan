# Generated by Django 4.1 on 2023-02-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conan_db_app', '0033_wiseword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='belong_to',
            field=models.ManyToManyField(blank=True, to='conan_db_app.affiliation'),
        ),
    ]
