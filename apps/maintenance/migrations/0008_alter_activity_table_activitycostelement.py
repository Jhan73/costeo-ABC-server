# Generated by Django 4.2.7 on 2023-11-22 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0007_activity'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='activity',
            table='maintenance_activities',
        ),
        migrations.CreateModel(
            name='ActivityCostElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=0)),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.activity')),
                ('cost_element_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.costelement')),
            ],
            options={
                'db_table': 'maintenance_activity_cost_elements',
            },
        ),
    ]
