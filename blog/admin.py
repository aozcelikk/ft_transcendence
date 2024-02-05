from django.contrib import admin
from .models import Kisiler


class KisilerAdmin(admin.ModelAdmin):
	list_display = ("kullanici", "tam_adi", "resim","cevrimici","slug",)
	list_editable = ("resim", "cevrimici",)
	search_fields = ("kullanici",)
	readonly_fields = ("slug",)
	list_filter = ("cevrimici",)


admin.site.register(Kisiler, KisilerAdmin)
