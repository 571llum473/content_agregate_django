# Generated by Django 3.1.2 on 2020-11-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_cntnt', '0012_auto_20201122_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='source',
            name='url_rss',
            field=models.URLField(),
        ),
    ]
