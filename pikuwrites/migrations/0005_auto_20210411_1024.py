# Generated by Django 3.1.5 on 2021-04-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pikuwrites', '0004_auto_20210315_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='poem', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.CharField(default='hindi', max_length=255),
        ),
    ]
