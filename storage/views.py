from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from storage.serializers import SequenceSerializer
from storage.models import Sequence

class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

    def create(self, request, *args, **kwargs):
        '''
        Can be reached by link http://localhost:8000/seq
        Validations: 
            both fields should be mandatory, 
            'sequence' should have only ACTGactg symbols
        '''
        sequence = request.data.get('sequence')
        for n in sequence:
            if n not in ['A','C','T','G','a','c','t','g']:
                return Response({'status': 'Failed', 'message': 'Sequence should contain only ACTG'})
        super().create(request, *args, **kwargs)
        return Response({'status':'Ok', 'message':'Sequence uploaded successfully'})
