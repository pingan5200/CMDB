# Generated by Django 2.1.4 on 2019-02-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='manufactory',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商'),
        ),
    ]
