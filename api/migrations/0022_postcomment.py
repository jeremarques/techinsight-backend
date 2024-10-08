# Generated by Django 5.0 on 2024-01-07 16:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_postlike_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('updated_at', models.DateTimeField(editable=False, null=True, verbose_name='updated at')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.userprofile')),
            ],
            options={
                'verbose_name': 'post comment',
                'verbose_name_plural': 'post comments',
            },
        ),
    ]
