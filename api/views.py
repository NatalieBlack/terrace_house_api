from api.models import Member, Series
from rest_framework import viewsets, permissions
from api.serializers import MemberSerializer, SeriesSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

