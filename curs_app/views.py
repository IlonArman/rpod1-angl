from django.shortcuts import render, get_object_or_404
from .models import Curs

def home_page(req):
    return render(req, "./home.html")

def cursy_page(req):
    cursy = Curs.objects.all()
    context = {
        'cursy': cursy
    }
    return render(req, "./cursy.html", context)


def aboutus_page(req):
    return render(req, "./aboutus.html")

def curs_details(req, pk):
    curs = get_object_or_404(Curs, pk=pk)
    context = {
        'curs': curs
    }
    return render(req, "./curs_details.html", context)
