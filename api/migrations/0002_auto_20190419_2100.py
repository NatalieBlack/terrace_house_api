# Generated by Django 2.2 on 2019-04-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name_en',
            new_name='full_name_en',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name_jp',
            new_name='full_name_jp',
        ),
        migrations.AddField(
            model_name='member',
            name='nickname_en',
            field=models.CharField(default='temp', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='nickname_jp',
            field=models.CharField(default='temp', max_length=255),
            preserve_default=False,
        ),
    ]
