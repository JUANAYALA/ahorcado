from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "pages/nuevo_juego.html", {})