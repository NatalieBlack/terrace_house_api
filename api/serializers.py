from api.models import Series, Member
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member 
        fields = ('full_name_en', 'full_name_jp', 'nickname_en', 'nickname_jp', 'series', 'start_week', 'end_week')


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Series
        fields = ('name', 'number')