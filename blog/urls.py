from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _


urlpatterns = [
	path("", views.index),
	path("index", views.index, name="ilksayfa"),
	path(_("anasayfa"), views.indexOO, name="anasayfa"),
	path(_("pingpong"), views.pingpong, name="pingpong"),
	path(_("kisiler"), views.kisiler, name="kisiler"),
	path(_("kisiler/<str:id>"), views.kisiler_detay, name="kisiler_detay"),
]
