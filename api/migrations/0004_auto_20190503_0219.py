# Generated by Django 2.2 on 2019-05-03 02:16

from django.db import migrations

def residencies(apps, schema_editor):
    Member = apps.get_model('api', 'Member')
    Residency = apps.get_model('api', 'Residency')
    for member in Member.objects.all():
        series = member.series
        sw = member.start_week
        ew = member.end_week
        Residency.objects.create(member=member, start_week=sw, end_week=ew, series=series)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_residency'),
    ]

    operations = [
        migrations.RunPython(residencies),
    ]