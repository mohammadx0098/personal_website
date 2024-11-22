# Generated by Django 4.0.7 on 2024-11-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='projects')),
            ],
        ),
    ]