# Generated by Django 4.1 on 2023-01-22 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conan_db_app', '0031_profession_affiliation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='affiliation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='conan_db_app.affiliation'),
        ),
    ]
