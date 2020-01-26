# Django
from django.urls import path

# Views
from curso_api_rest.publications.views.publications import list_publications

urlpatterns = [
    path("publications/", list_publications)
]
