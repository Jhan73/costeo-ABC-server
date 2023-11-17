# Generated by Django 4.2.7 on 2023-11-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCenter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inductor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('state', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_user', models.CharField(max_length=255)),
            ],
        ),
    ]
