# Generated by Django 4.2.7 on 2023-11-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_costing_rename_state_costobject_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directlaborcostobject',
            old_name='cant',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='directrawmaterialcostobject',
            old_name='cant',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='directservicecostobject',
            old_name='cant',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='activitycostobject',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='activitycostobject',
            table='process_activity_cost_objects',
        ),
        migrations.AlterModelTable(
            name='costobject',
            table='process_cost_objects',
        ),
        migrations.AlterModelTable(
            name='directlaborcostobject',
            table='process_direct_labor_cost_objects',
        ),
        migrations.AlterModelTable(
            name='directrawmaterialcostobject',
            table='process_direct_raw_material_cost_objects',
        ),
        migrations.AlterModelTable(
            name='directservicecostobject',
            table='process_direct_service_cost_objects',
        ),
    ]
