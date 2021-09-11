from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

from storage.serializers import SequenceSerializer
from storage.models import Sequence

class SequenceList(ListAPIView):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

class SequenceCreate (CreateAPIView):
    serializer_class = SequenceSerializer

    def create(self, request, *args, **kwargs):
        sequence = request.data.get('sequence')
        for n in sequence:
            if n not in ['A','C','T','G','a','c','t','g']:
                raise ValidationError({'sequence': 'Should contain only ACTG'})
        return super().create(request, *args, **kwargs)