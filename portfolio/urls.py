from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'portfolio'
urlpatterns=[
    url(r'^$', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)