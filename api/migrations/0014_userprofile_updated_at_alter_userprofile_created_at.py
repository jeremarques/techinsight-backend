# Generated by Django 5.0 on 2024-01-05 15:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='Data de atualização'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined'),
        ),
    ]
