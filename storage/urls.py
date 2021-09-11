from django.urls import include, __path__
from django.urls.conf import path
from rest_framework import routers, urlpatterns

from storage.views import SequenceViewSet

router = routers.DefaultRouter()
router.register(r'sequences', SequenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]