from api.models import Series, Member
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member 
        fields = ('name_en', 'name_jp', 'series', 'start_week', 'end_week')


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Series
        fields = ('name', 'number')