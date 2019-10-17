# Generated by Django 2.2.6 on 2019-10-17 21:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0837b07f-e94a-4380-abfb-39ea475d3ecd'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='marca',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e18fdd1-ac3b-4222-8ee0-1f4922c7da29'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6c4089c2-f7f9-4544-a3af-748b3730e3db'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solicitante',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0340a3e8-c4df-4839-8550-1a13238a6a81'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='cantidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='id',
            field=models.UUIDField(default=uuid.UUID('43c349e0-b97e-4c2f-a968-c27c91c1845e'), editable=False, primary_key=True, serialize=False),
        ),
    ]