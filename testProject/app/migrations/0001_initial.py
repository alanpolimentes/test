# Generated by Django 2.2.6 on 2019-10-17 20:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('marca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('producto', models.ManyToManyField(to='app.Producto')),
                ('solicitante', models.ManyToManyField(to='app.Solicitante')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Subcategoria'),
        ),
    ]
