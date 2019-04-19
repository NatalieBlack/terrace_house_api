from django.db import models

# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Member(models.Model):
    full_name_en = models.CharField(max_length=255)
    nickname_en = models.CharField(max_length=255)
    full_name_jp = models.CharField(max_length=255)
    nickname_jp = models.CharField(max_length=255)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    start_week = models.IntegerField()
    end_week = models.IntegerField()
