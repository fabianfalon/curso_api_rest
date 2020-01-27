from rest_framework import serializers

from curso_api_rest.publications.serializers.categories import CategorySerializer

class PublicationSerializer(serializers.Serializer):
    """PublicationSerializer"""
    title = serializers.CharField()
    description = serializers.CharField()
    type_of_publication = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    is_active = serializers.BooleanField()
    category = CategorySerializer()