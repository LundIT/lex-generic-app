# Generated by Django 4.1.13 on 2024-06-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    A class representing a database migration.

    This migration includes the creation of two new models and the addition of fields to existing models.

    Attributes
    ----------
    dependencies : list
        A list of migration dependencies.
    operations : list
        A list of operations to be applied during the migration.
    """

    dependencies = [
        ('generic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationIDs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('context_id', models.TextField(default='test_id')),
                ('calculation_record', models.TextField()),
                ('calculation_id', models.TextField(default='test_id')),
            ],
        ),
        migrations.CreateModel(
            name='ModificationRestrictedModelExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='calculationlog',
            name='calculation_record',
            field=models.TextField(default='legacy'),
        ),
        migrations.AddField(
            model_name='userchangelog',
            name='calculation_record',
            field=models.TextField(default='legacy'),
        ),
    ]
