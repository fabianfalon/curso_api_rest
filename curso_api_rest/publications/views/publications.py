from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from curso_api_rest.publications.models import Publication

# Serializers
from curso_api_rest.publications.serializers import PublicationSerializer


@api_view(["GET"])
def list_publications(request):
    """List publications"""
    publications = Publication.objects.all()
    serializer = PublicationSerializer(publications, many=True)
    return Response(serializer.data)
