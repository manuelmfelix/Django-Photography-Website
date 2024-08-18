from django.contrib import admin
from django.urls import path, include
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('portfolio/<int:catalog_id>', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('portfolio/api/', include('portfolio.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
