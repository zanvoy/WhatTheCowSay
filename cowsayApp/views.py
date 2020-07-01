from django.shortcuts import render, HttpResponseRedirect
from cowsayApp.forms import CowAddForm
from cowsayApp.models import WhatTheCowsay
import subprocess

# Create your views here.
def index(request):
    html = 'index.html'

    if request.method == 'POST':
        form = CowAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            WhatTheCowsay.objects.create(
               what_does_the_cowsay = 
               subprocess.run(['cowsay', data['what_does_the_cowsay']], capture_output = True, text = True).stdout 
            )
            cow = WhatTheCowsay.objects.last()
            form = CowAddForm()
            return render(request, html, {'form': form, 'cow': cow})

    form = CowAddForm()
    return render(request, html, {'form': form})

def history(request):
    if len(WhatTheCowsay.objects.all()) < 10:
        data = WhatTheCowsay.objects.all().order_by('-id')
    else:
        data = WhatTheCowsay.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'data': data})
