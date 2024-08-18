from rest_framework import serializers
from .models import Catalog, Photo

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'year', 'description','camera','lens']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['index', 'title', 'image', 'description', 'catalog', 'exposure', 'focal_distance', 'iso', 'is_cover_image']
