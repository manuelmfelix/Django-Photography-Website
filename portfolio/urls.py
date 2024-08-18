# myapp/urls.py
from django.urls import path
from .views import create_catalog, create_photo, catalog_list, catalog_photos, delete_catalog, update_catalog

urlpatterns = [
    path('catalogs/', create_catalog, name='create_catalog'),
    path('photos/', create_photo, name='create_photo'),
    path('catalogs/list/', catalog_list, name='catalog_list'),
    path('catalogs/<int:catalog_id>/photos/', catalog_photos, name='catalog_photos'),
    path('catalogs/<int:catalog_id>/', update_catalog, name='catalog-update'),
    path('catalogs/delete/', delete_catalog, name='catalog-delete-all'),
    path('catalogs/delete/<int:catalog_id>/', delete_catalog, name='catalog-delete-specific'),
]
