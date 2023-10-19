from rest_framework import serializers
from .models import CD

class CDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CD
        fields = ['id', 'album', 'artist', 'year']