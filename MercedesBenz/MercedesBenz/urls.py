from django.contrib import admin
from django.urls import path

from posts.views import index, home
from landingpage.views import indexcar, motorlistview
from blog.views import Blog

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('home/', home),
    path('cars/', indexcar),
    path('motors/', motorlistview),
    path('blog/' , Blog)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)