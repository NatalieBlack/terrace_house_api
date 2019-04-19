# Generated by Django 2.2 on 2019-04-19 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255)),
                ('name_jp', models.CharField(max_length=255)),
                ('start_week', models.IntegerField()),
                ('end_week', models.IntegerField()),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Series')),
            ],
        ),
    ]
