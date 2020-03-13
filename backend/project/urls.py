from django.contrib import admin
from django.urls import path, include
from core.views import SnippetDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("core.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', SnippetDetail.as_view())
]
