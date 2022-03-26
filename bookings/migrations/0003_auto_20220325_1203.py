# Generated by Django 3.2 on 2022-03-25 12:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_rename_reserve_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-check_in']},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
