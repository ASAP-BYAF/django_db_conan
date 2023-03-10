# Generated by Django 4.1 on 2023-01-17 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conan_db_app', '0020_remove_case_cause_of_death_remove_case_motivation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='belong_to',
            field=models.CharField(choices=[('teitan_elementary_school', '帝丹小学校'), ('teitan_high_school', '帝丹高校'), ('touto_university', '東都大学'), ('black', '黒の組織'), ('mouri', '毛利家'), ('police', '警察'), ('fbi', 'FBI'), ('sis', 'SIS'), ('noc', 'NOC'), ('red', '赤井家')], default='fbi', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='kind',
            field=models.CharField(choices=[('black', '黒の組織'), ('love', '恋愛'), ('police', '警察関係'), ('kid', 'キッド'), ('fbi', 'FBI'), ('red', '赤井家')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='profession',
            field=models.CharField(choices=[('elementary_school_student', '小学生'), ('high_school_student', '高校生'), ('police', '警察官'), ('private_eye', '探偵'), ('fbi', 'FBI捜査官')], max_length=30, null=True),
        ),
    ]
