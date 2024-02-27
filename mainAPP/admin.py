from django.contrib import admin
from .models import *



class TransfersAdmin(admin.ModelAdmin):
    list_display = ["id","player","club_eski","club_yangi","narx","taxmin_narx","sana","mavsum"]
    list_display_links = ["id","player"]
    list_editable = ["club_yangi" , "club_eski"]
    list_filter = ["mavsum"]
    search_fields = ["player"]
    search_help_text = "Playerni qidiring."
    list_per_page = 4


admin.site.register(Davlat)
admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Transfer,TransfersAdmin)


