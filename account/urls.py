from django.urls import path,include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

urlpatterns = [
	path(_("giris"), views.login_request, name="giris"),
	path(_("kayit"), views.register_request, name="kayit"),
	path(_("cikis"), views.logout_request, name="cikis"),
	path(_("kullanici"),views.auth_settings, name="kullanici"),
	path(_("accounts"), include('django.contrib.auth.urls')),
	path(_("sifre"),views.sifre, name="sifre"),
	path(_("adi"),views.adi, name="adi"),
	path(_("email"),views.email, name="email"),
	path(_("resim"),views.resim, name="resim"),
]
