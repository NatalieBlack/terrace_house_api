from api.models import Series, Member, Residency
from rest_framework import serializers


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'name', 'number')

class ResidencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Residency 
        fields = ('id', 'start_week', 'end_week', 'series', 'member')

class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member 
        fields = ('id', 'full_name_en', 'full_name_jp', 'nickname_en', 'nickname_jp', 'residencies')