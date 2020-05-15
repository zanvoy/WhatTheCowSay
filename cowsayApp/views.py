from django.shortcuts import render, HttpResponseRedirect
from cowsayApp.forms import CowAddForm
from cowsayApp.models import WhatTheCowsay

# Create your views here.
def index(request):
    html = 'index.html'

    if request.method == 'POST':
        form = CowAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            WhatTheCowsay.objects.create(
               what_does_the_cowsay = ['what_does_the_cowsay'] 
            )
            return HttpResponseRedirect('/')

    form = CowAddForm()
    return render(request, html, {'form': form})