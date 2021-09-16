from django.contrib import admin
from django.urls import path, include

import storage.views
import storage.api_views

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('', include('storage.urls')),
    path('v2/api/', storage.api_views.SequenceList.as_view()),
    path('v2/api/new', storage.api_views.SequenceCreate.as_view())
]
