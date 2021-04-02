from django.shortcuts import render
from .forms import ContactForm

from django.http import HttpResponse
import datetime


# Create your views here.
def cadastroCreateView(request):
    context = {}
    form = ContactForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form'] = form

    return render(request, "cadastro.html", context)


def hora_atual(request):
    agora: datetime = datetime.datetime.now()
    html = "<h1>Agora são: %s</h1>" % agora.strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(html)
