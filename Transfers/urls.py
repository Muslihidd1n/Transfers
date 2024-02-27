from django.contrib import admin
from django.urls import path
from mainAPP.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('clubs/', clubs, name='clubs'),
    path('players/', players, name='players'),
    path('u20_players/', u20_players, name='u20_players'),
    path('seasons/', seasons, name='seasons'),
    path('<str:country_name>/clubs/', country_clubs),
    path('latest_transfers/', transfers, name='latest-transfers'),
    path('tryouts/', tryouts, name='tryouts'),
    path('about/', about , name='about'),
    path('stats/', stats , name='stats'),
    path('transfer-archive/', transfer_archive , name='transfer-archive'),
    path('top_50_clubs/',top_50_clubs),
    path('transfers_record/',transfers_record),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

