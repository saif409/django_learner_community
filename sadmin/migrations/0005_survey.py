# Generated by Django 3.1.7 on 2021-04-10 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0004_auto_20210408_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person_name', models.CharField(max_length=200)),
                ('contact_person_email', models.CharField(max_length=200)),
                ('contact_person_phone', models.CharField(max_length=200)),
                ('comapany_name', models.CharField(max_length=200)),
                ('company_address', models.CharField(max_length=200)),
                ('company_email', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('surveyor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.surveyor')),
            ],
        ),
    ]
