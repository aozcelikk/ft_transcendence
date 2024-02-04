from django.contrib import admin
from .models import Kisiler


class KisilerAdmin(admin.ModelAdmin):
	list_display = ("kullanici", "tam_adi", "resim","cevrimici","engel","slug",)
	list_editable = ("resim", "cevrimici","engel",)
	search_fields = ("kullanici",)
	readonly_fields = ("slug",)
	list_filter = ("cevrimici", "engel",)


admin.site.register(Kisiler, KisilerAdmin)

