# Generated by Django 5.0 on 2024-01-02 22:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('name', models.CharField(max_length=60)),
                ('bio', models.CharField(blank=True, max_length=200)),
                ('about', models.TextField(blank=True)),
                ('date_of_birth', models.DateField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]