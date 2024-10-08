# Generated by Django 5.0 on 2024-01-08 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_post_likes_counter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'ordering': ['-created_at'], 'verbose_name': 'post comment', 'verbose_name_plural': 'post comments'},
        ),
    ]
