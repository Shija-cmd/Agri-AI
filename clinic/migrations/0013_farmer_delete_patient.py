# Generated by Django 5.0.1 on 2024-07-04 18:32

import clinic.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_alter_patient_hospitali_alter_patient_jinsia'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True, null=True)),
                ('farm_id', models.CharField(db_index=True, default=clinic.models.generate_random_code, editable=False, max_length=9)),
                ('N', models.PositiveIntegerField(max_length=15)),
                ('P', models.PositiveIntegerField(max_length=15)),
                ('K', models.PositiveIntegerField(max_length=15)),
                ('temperature', models.PositiveIntegerField(max_length=15)),
                ('humidity', models.PositiveIntegerField(max_length=15)),
                ('ph', models.PositiveIntegerField(max_length=15)),
                ('rainfall', models.PositiveIntegerField(max_length=15)),
                ('label', models.CharField(blank=True, editable=False, max_length=100)),
                ('complete', models.BooleanField(default=False, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['complete'],
            },
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
