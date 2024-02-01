from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

urlpatterns = [
	path(_("giris"), views.login_request, name="giris"),
	path(_("kayit"), views.register_request, name="kayit"),
	path(_("cikis"), views.logout_request, name="cikis"),
]
