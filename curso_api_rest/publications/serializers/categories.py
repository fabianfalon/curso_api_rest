from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    """CategorySerializer"""
    id = serializers.IntegerField()
    name = serializers.CharField()