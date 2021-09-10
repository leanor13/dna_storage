# import storage
from django.shortcuts import render
# from django.http import HttpResponse
from storage.models import Sequence

def index(request):
    sequences = Sequence.objects.all()
    return render(request, 'pages/index.html', {
        'sequences': sequences,
    })
 