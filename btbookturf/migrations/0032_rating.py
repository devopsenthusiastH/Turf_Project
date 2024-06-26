# Generated by Django 4.1.7 on 2024-04-18 18:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btbookturf', '0031_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('feedback', models.TextField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btbookturf.booking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btbookturf.myusers')),
            ],
        ),
    ]
