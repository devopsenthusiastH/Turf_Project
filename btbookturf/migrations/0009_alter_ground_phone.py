# Generated by Django 4.1.4 on 2023-03-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btbookturf', '0008_alter_booking_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ground',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
