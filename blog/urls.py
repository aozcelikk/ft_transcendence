from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _
from django.conf.urls.static import static
from django.urls import re_path


urlpatterns = [
	path("", views.indexOO),
	path("index", views.index, name="ilksayfa"),
	path(_("anasayfa"), views.indexOO, name="anasayfa"),
	path(_("pingpong"), views.pingpong, name="pingpong"),
	path(_("kisiler"), views.kisiler, name="kisiler"),
	path(_("kisiler/cevrimici"), views.cevrimici, name="cevrimici"),
	path(_("kisiler/arkadaslar"), views.arkadaslar, name="arkadaslar"),
	path(_("kisiler/engellenenler"), views.engellenenler, name="engellenenler"),
	path(_("kisiler/<slug:slug>"), views.kisiler_detay, name="kisiler_detay"),
	re_path(r'^kisiler/arkadaslar/(?P<alternatif>.+)/(?P<pk>\d+)/$', views.arkadas_sistem, name="arkadas_sistem"),
	re_path(r'^kisiler/engellenenler/(?P<opsiyon>.+)/(?P<pk>\d+)/$', views.engel_sistem, name="engel_sistem"),
]
