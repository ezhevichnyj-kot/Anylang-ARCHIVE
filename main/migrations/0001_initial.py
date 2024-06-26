# Generated by Django 5.0.4 on 2024-04-22 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unnamed', max_length=255)),
                ('file', models.FileField(upload_to='upldfile/')),
            ],
        ),
        migrations.CreateModel(
            name='TranslateArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upldfile/')),
                ('lang', models.CharField(max_length=255)),
                ('orig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
            ],
        ),
    ]
