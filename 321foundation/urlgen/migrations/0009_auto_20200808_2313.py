# Generated by Django 2.2.13 on 2020-08-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlgen', '0008_auto_20200808_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='urlgenerated',
            field=models.CharField(max_length=255),
        ),
    ]
