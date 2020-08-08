# Generated by Django 2.2.13 on 2020-08-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='numberDailySchoolViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_name', models.CharField(max_length=200)),
                ('school_name', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('views', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='numberTeacherViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('views', models.IntegerField()),
            ],
        ),
    ]