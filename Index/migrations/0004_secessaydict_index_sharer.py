# Generated by Django 2.0 on 2019-11-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0003_auto_20191112_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='secessaydict',
            name='index_sharer',
            field=models.CharField(blank=True, max_length=25, verbose_name='分享者'),
        ),
    ]
