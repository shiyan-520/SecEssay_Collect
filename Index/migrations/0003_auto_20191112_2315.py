# Generated by Django 2.0 on 2019-11-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_auto_20191112_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secessaydict',
            name='index_type',
            field=models.CharField(max_length=25, verbose_name='分类'),
        ),
    ]
