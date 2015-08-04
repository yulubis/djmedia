from django.conf.urls import include, url
from vizor.admin import admin_site
from vizor import views

urlpatterns = [
    url(r'^admin/', include(admin_site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^upload/$', views.upload_handler, name="upload"),
    url(r'^download/(?P<filename>.+)$', views.download, name="download"),
]
