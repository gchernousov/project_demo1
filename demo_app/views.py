from django.shortcuts import render

from .models import Data

def index(request):
    values = Data.objects.all()
    context = {'data': values}
    return render(request, template_name='demo_app/index.html', context=context)
