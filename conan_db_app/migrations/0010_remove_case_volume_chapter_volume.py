# Generated by Django 4.1 on 2022-11-22 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conan_db_app', '0009_remove_case_id_remove_volume_id_alter_case_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='volume',
        ),
        migrations.AddField(
            model_name='chapter',
            name='volume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='conan_db_app.volume'),
        ),
    ]
