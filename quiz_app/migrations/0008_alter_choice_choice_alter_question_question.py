# Generated by Django 4.2.6 on 2023-11-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_remove_profile_publisher_alter_choice_is_correct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.CharField(max_length=100, verbose_name='choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=250, verbose_name='question'),
        ),
    ]
