# Generated by Django 2.2.6 on 2019-10-16 21:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191016_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]