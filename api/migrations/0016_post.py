# Generated by Django 5.0 on 2024-01-05 18:54

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_posttag_updated_at_alter_posttag_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.CharField(max_length=14, unique=True, verbose_name='ID usado para as urls dos posts')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120)),
                ('content', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Quantidade de likes do post')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('updated_at', models.DateTimeField(editable=False, null=True, verbose_name='Data de atualização')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.userprofile')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='api.posttag')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
