from rest_framework.decorators import api_view
from rest_framework.response import Response

from curso_api_rest.publications.models import Publication


@api_view(["GET"])
def list_publications(request):
    """List publications"""
    publications = Publication.objects.all()
    data = []
    for publication in publications:
        data.append({
            "title": publication.title,
            "description": publication.description,
            "type_of_publication": publication.type_of_publication,
            "price": publication.price,
            "is_active": publication.is_active
        })
    return Response(data)
