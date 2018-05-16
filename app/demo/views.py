from django.shortcuts import render

# Create your views here.
from demo import forms
from demo.forms import HouseQueryForm


def basic(request):
    if request.method == 'POST':
        form = HouseQueryForm(request.POST)
    else:
        form = HouseQueryForm()

    return render(request, 'demo/base.html',
                  {'name': 'Basic', 'form': form})


def home(request):
    search_form = forms.process_queryform(request)

    return render(request, 'demo/base.html',
                  {'name': 'Search', 'form': search_form})


def links(request):
    return render(request, 'demo/home.html', {})


def search(request, link=None):
    search_form = forms.process_queryform(request, link)

    return render(request, 'demo/search.html',
                  {'name': 'Results', 'form': search_form})


def detail(request):
    search_form = forms.process_queryform(request)

    return render(request, 'demo/detail.html',
                  {'name': 'Detail', 'form': search_form})
