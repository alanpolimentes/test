# Generated by Django 2.2.6 on 2019-10-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191016_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='subcategoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='subcategoria',
            field=models.ManyToManyField(default=None, to='app.Subcategoria'),
        ),
    ]