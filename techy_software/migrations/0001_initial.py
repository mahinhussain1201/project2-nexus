# Generated by Django 5.0.1 on 2024-01-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('author', models.TextField(default='No author available')),
                ('date', models.DateField()),
                ('heading', models.TextField(default='No heading available')),
                ('content', models.TextField(default='No content available')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='No content available')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.TextField(default='No name available')),
                ('country', models.TextField(default='No country available')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('type', models.TextField(default='Not available')),
                ('heading', models.TextField(default='No heading available')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('heading', models.TextField(default='No heading available')),
                ('content', models.TextField(default='No content available')),
            ],
        ),
    ]
