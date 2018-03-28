# Generated by Django 2.0.3 on 2018-03-19 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=30)),
                ('tel_num', models.IntegerField()),
                ('num_people', models.IntegerField()),
                ('rend_date', models.DateTimeField()),
                ('rend_time', models.SmallIntegerField(choices=[(0, '9:00 ~ 10:00'), (1, '10:00 ~ 11:00'), (2, '11:00 ~ 12:00'), (3, '12:00 ~ 13:00'), (4, '13:00 ~ 14:00'), (5, '14:00 ~ 15:00'), (6, '15:00 ~ 16:00'), (7, '16:00 ~ 17:00'), (8, '17:00 ~ 18:00'), (9, '18:00 ~ 19:00'), (10, '19:00 ~ 20:00')], default=0)),
                ('return_date', models.DateTimeField()),
                ('return_time', models.SmallIntegerField(choices=[(0, '9:00 ~ 10:00'), (1, '10:00 ~ 11:00'), (2, '11:00 ~ 12:00'), (3, '12:00 ~ 13:00'), (4, '13:00 ~ 14:00'), (5, '14:00 ~ 15:00'), (6, '15:00 ~ 16:00'), (7, '16:00 ~ 17:00'), (8, '17:00 ~ 18:00'), (9, '18:00 ~ 19:00'), (10, '19:00 ~ 20:00')], default=0)),
                ('room_number', models.SmallIntegerField()),
                ('reservation_accept', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]