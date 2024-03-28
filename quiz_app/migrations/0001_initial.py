# Generated by Django 4.2.6 on 2023-10-25 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50, verbose_name='Choice')),
                ('position', models.IntegerField(verbose_name='position')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.question')),
            ],
            options={
                'ordering': ('position',),
                'unique_together': {('question', 'position'), ('question', 'choice')},
            },
        ),
    ]