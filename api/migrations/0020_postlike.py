# Generated by Django 5.0 on 2024-01-07 15:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_rename_likes_post_likes_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.userprofile')),
            ],
            options={
                'verbose_name': 'post tag',
                'verbose_name_plural': 'post tags',
            },
        ),
    ]