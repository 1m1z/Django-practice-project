from django.contrib import admin
from django.urls import path

from posts.views import home,homemenu
from landingpage.views import indexcar, motorlistview
from blog.views import Bloglistview,BlogListDetailsVeiw

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homemenu),
    path('cars/', indexcar),
    path('motors/', motorlistview),
    path('blog/' , Bloglistview),
    path('blog/blogdetails/<int:post_id>' , BlogListDetailsVeiw)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)