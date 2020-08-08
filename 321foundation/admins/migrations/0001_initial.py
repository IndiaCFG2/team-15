# Generated by Django 3.0.7 on 2020-08-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(default='incomplete', max_length=100)),
            ],
        ),
    ]
