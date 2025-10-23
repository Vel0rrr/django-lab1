
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_blog.urls')),   # всі запити в корені підуть в app_blog.urls
]