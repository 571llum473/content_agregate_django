# Generated by Django 3.1.2 on 2020-11-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_cntnt', '0011_profile_love_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='source',
            name='url_rss',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(default=None),
        ),
    ]