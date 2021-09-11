from rest_framework import serializers

from storage.models import Sequence

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = ('name', 'sequence')
