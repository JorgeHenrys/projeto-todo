# Generated by Django 3.0.6 on 2020-05-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'FAZENDO'), ('done', 'FEITO')], max_length=5),
        ),
    ]
