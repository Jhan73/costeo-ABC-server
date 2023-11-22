# Generated by Django 4.2.7 on 2023-11-21 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0006_directlabor_directrawmaterial_directservice_and_more'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costobject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='costobject',
            name='created_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='costobject',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='costobject',
            name='updated_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterModelTable(
            name='costobject',
            table='Process_cost_objects',
        ),
        migrations.CreateModel(
            name='DirectServiceCostObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.costobject')),
                ('direct_service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.directservice')),
            ],
            options={
                'db_table': 'Process_direct_service_cost_objects',
            },
        ),
        migrations.CreateModel(
            name='DirectRawMaterialCostObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField()),
                ('cost_object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.costobject')),
                ('direct_raw_material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.directrawmaterial')),
            ],
            options={
                'db_table': 'Process_direct_raw_material_cost_objects',
            },
        ),
        migrations.CreateModel(
            name='DirectLaborCostObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField()),
                ('cost_object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.costobject')),
                ('direct_labor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.directlabor')),
            ],
            options={
                'db_table': 'Process_direct_labor_cost_objects',
            },
        ),
    ]