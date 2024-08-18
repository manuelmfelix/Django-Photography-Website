from django.shortcuts import render, get_object_or_404
from .models import Photo, Catalog
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Catalog, Photo
from .serializers import CatalogSerializer, PhotoSerializer

def home(request):
    catalogs = Catalog.objects.all().order_by('year')
    return render(request, 'portfolio/home.html', {'catalogs': catalogs})

def portfolio(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    photos = Photo.objects.filter(catalog=catalog)
    return(render(request, 'portfolio/portfolio.html', {'photos':photos, 'catalog':catalog}))

def about(request):
     return render(request, 'portfolio/about.html')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_catalog(request):
    if request.method == 'POST':
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_photo(request):
    if request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def catalog_list(request):
    catalogs = Catalog.objects.all()
    serializer = CatalogSerializer(catalogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def catalog_photos(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    photos = Photo.objects.filter(catalog=catalog)
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_catalog(request, catalog_id=None):
    if catalog_id:
        # Delete specific catalog
        try:
            catalog = Catalog.objects.get(id=catalog_id)
            catalog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Catalog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        # Delete all catalogs
        Catalog.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_catalog(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    serializer = CatalogSerializer(catalog, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)