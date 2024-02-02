from django.contrib import admin
from .models import Kisiler,Kategori


class KisilerAdmin(admin.ModelAdmin):
	list_display = ("kullanici", "tam_adi", "resim","cevrimici","engel","slug","secili_kategoriler",)
	list_editable = ("resim", "cevrimici","engel",)
	search_fields = ("kullanici",)
	readonly_fields = ("slug",)
	list_filter = ("cevrimici", "engel", "kategoriler",)

	def secili_kategoriler(self, obj):
		html = ""
		for kategori in obj.kategoriler.all():
			html += kategori.name + " "

		return html



admin.site.register(Kisiler, KisilerAdmin)
admin.site.register(Kategori)
