'''
This file is not used at the moment, refer to views.py
'''
from django.db.models import query
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from storage.serializers import SequenceSerializer
from storage.models import Sequence

class SequenceList(ListAPIView):
#    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

    def get_queryset(self):
        """
        Get list of sequences with specific name. 
        Format: http://localhost:8000/v2/api/?name=<name>
        """
        queryset = Sequence.objects.all()
        seq_name = self.request.query_params.get('name')
        if seq_name is not None:
            queryset = queryset.filter(name = seq_name)
        return queryset

 
class SequenceCreate(CreateAPIView):
    serializer_class = SequenceSerializer

    def create(self, request, *args, **kwargs):
        '''
        Can be reached by link http://localhost:8000/v2/api/new
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


