# Generated by Django 3.1.6 on 2021-04-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0006_auto_20210410_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='surveyor',
            field=models.CharField(max_length=200),
        ),
    ]