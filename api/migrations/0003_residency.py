# Generated by Django 2.2 on 2019-05-03 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190419_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_week', models.IntegerField()),
                ('end_week', models.IntegerField(null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residences', to='api.Member')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residencies', to='api.Series')),
            ],
        ),
    ]
