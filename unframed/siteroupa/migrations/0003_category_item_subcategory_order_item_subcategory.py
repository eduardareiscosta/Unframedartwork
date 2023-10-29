# Generated by Django 4.2.6 on 2023-10-28 18:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteroupa', '0002_customuser_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('color', models.CharField(max_length=30)),
                ('stock', models.IntegerField(default=0)),
                ('onsale', models.BooleanField(default=False)),
                ('pub_data', models.DateTimeField(default=datetime.datetime(2023, 10, 28, 18, 10, 0, 302613, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='siteroupa.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=15)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 10, 28, 18, 10, 0, 302613, tzinfo=datetime.timezone.utc))),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteroupa.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='siteroupa.subcategory'),
        ),
    ]
