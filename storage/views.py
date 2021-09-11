from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from storage.serializers import SequenceSerializer
from storage.models import Sequence

class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

'''
class SequenceList(APIView):

    def get(self, request):



    def post(self):
        pass
'''