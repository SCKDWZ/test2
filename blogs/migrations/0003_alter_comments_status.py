# Generated by Django 3.2.16 on 2025-02-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20250213_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (2, '冻结')], default=1, verbose_name='状态'),
        ),
    ]
