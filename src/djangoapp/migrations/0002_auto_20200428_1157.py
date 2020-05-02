# Generated by Django 3.0.5 on 2020-04-28 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='id',
        ),
        migrations.AlterField(
            model_name='price',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='djangoapp.Item', unique=True, verbose_name='item'),
        ),
    ]