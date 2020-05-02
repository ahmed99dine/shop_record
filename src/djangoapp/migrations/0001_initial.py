# Generated by Django 3.0.5 on 2020-04-22 10:27

from django.db import migrations, models
import django.db.models.deletion
import djangoapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(default=djangoapp.models.random_string_generator, max_length=100, primary_key=True, serialize=False)),
                ('model_no', models.CharField(blank=True, max_length=10, null=True)),
                ('make', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('sell', models.FloatField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.Item', unique=True)),
            ],
        ),
    ]