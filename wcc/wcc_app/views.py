from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from wcc_app.models import Tocht

def index(request):
    alle_tochten = Tocht.objects.order_by('datum')
    context = {'alle_tochten_list': alle_tochten}
    return render(request, 'wcc_app/index.html', context)

def detail(request, tocht_id):
    tocht = get_object_or_404(Tocht, pk=tocht_id)
    return render(request, "wcc_app/detail.html", {'tocht': tocht})

def results(request, tocht_id):
    response = "Hier zijn de wandelaars van %s."
    return HttpResponse(response % tocht_id)