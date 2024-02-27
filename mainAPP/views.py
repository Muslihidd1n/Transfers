from django.shortcuts import render
from mainAPP.models import *
from datetime import date


def index(request):
    return render(request, "index.html")


def clubs(request):
    context = {
        "clubs": Club.objects.all()
    }
    return render(request,"clubs.html",context)


def players(request):
    content = {
        "players": Player.objects.order_by("-narx").all()
    }
    return render(request,"players.html",content)


def u20_players(request):
    hozirgi_sana = str(date.today())
    yil = int(hozirgi_sana[:4]) - 20
    yangi_sana = hozirgi_sana.replace(hozirgi_sana[:4], str(yil))
    content = {
        "u20_players": Player.objects.order_by("-narx").filter(t_yil__gt=yangi_sana)
    }
    return render(request,"U-20 players.html",content)


def seasons(request):
    mavsumlar = Transfer.objects.all().values_list('mavsum', flat=True)
    content = {
        'mavsumlar': sorted(mavsumlar)
    }
    return render (request,"transfer-archive.html", content)


def country_clubs(request, country_name):
    content = {
        'clubs': Club.objects.filter(davlat__nom__contains=country_name)
    }
    return render(request, "country-clubs.html",content)


def transfers(request):
    hozirgi_sana = str(date.today())
    yil = hozirgi_sana[:4]
    content = {
        "transfers": Transfer.objects.order_by('-narx').filter(mavsum__contains=yil)
    }
    return render(request,"latest-transfers.html",content)


def tryouts(request):
    return render(request,"tryouts.html")


def about(request):
    return render(request,"about.html")


def stats(request):
    return render(request, 'stats.html')

def transfer_archive(request):
    return render(request, "transfer-archive.html")


def top_50_clubs(request):
    context = {
        'clubs': Club.objects.order_by('-kapital')[:50]
    }
    return render(request, "top_50_clubs_by_income.html",context)

def transfers_record(request):
    context={
        'players': Transfer.objects.order_by('-narx').filter(narx__gte=50)[:100]
    }
    return render(request, 'transfer-records.html', context)

