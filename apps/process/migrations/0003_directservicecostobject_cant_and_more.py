# Generated by Django 4.2.7 on 2023-11-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_alter_costobject_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='directservicecostobject',
            name='cant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='directlaborcostobject',
            name='cant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='directrawmaterialcostobject',
            name='cant',
            field=models.IntegerField(default=0),
        ),
    ]
