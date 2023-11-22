# Generated by Django 4.2.7 on 2023-11-21 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0006_directlabor_directrawmaterial_directservice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_user', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_user', models.CharField(blank=True, max_length=255, null=True)),
                ('activity_center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.activitycenter')),
            ],
        ),
    ]