# Generated by Django 3.0.6 on 2020-06-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shbm_api', '0002_host_heartrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]