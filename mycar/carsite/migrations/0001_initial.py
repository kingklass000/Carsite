# Generated by Django 5.1.2 on 2024-10-16 13:21

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True, verbose_name='в наличий')),
                ('product_video', models.FileField(blank=True, null=True, upload_to='', verbose_name='видео')),
                ('body', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=32)),
                ('engine', models.CharField(max_length=32)),
                ('box', models.CharField(max_length=32)),
                ('drive', models.CharField(max_length=32)),
                ('fuel_consumption', models.CharField(max_length=32)),
                ('acceleration', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=16, unique=True)),
                ('marca_name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('date_registered', models.DateField(auto_now=True, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('status', models.CharField(choices=[('pro', 'Pro'), ('simple', 'Simple')], default='simple', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CarPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='carsite.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='carsite.category'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='carsite.car')),
                ('parent_review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='carsite.review')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carsite.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Рейтинг')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='carsite.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carsite.userprofile')),
            ],
        ),
    ]
