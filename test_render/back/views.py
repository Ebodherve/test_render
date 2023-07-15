from django.shortcuts import render
from back.models import AnythingModel

# Create your views here.


def returnSimplePage(request):
    allmodels = AnythingModel.objects.all()
    return render(request, "back/index.html", context={"simples":allmodels})


