from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse 
from django.views import generic
from .models import Card, FirstDispute
from .forms import CardForm
from .filters import CardFilter
from django.template import Context, Template
import csv
from django import forms 
from django.contrib.admin.widgets import AdminDateWidget



def search(request):
    if request.method == "POST":
        treatment = request.POST['treatment']
        card_list = Card.objects.filter(case_number__contains=treatment)
        return render(request, 'main/search.html', {'treatment':treatment, 'card_list':card_list, 'title':'Результаты поискового запроса ',})
    else: 
        return render(request, 'main/search.html', {})


def show_card(request, card_id):
    card = Card.objects.get(pk=card_id) #primary key
    return render(request, 'main/show_card.html', {'card':card, 'title':'Карточки',})

def index(request):
    card_list = Card.objects.all().order_by('date')
    dispute = FirstDispute.objects.all()
    myFilter = CardFilter(request.GET, queryset=card_list)
    card_list = myFilter.qs
    return render(request, 'main/index.html', {"title":"Интернет-база постановлений судов", 'card_list':card_list, "myFilter":myFilter, 'dispute':dispute,})


def card_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=Cards.txt'
	# Designate The Model
	cards = Card.objects.all()
	lines = []
	# Loop Thu and output
	for card in cards:
		lines.append(f'{card.name}\n{card.case_number}\n{card.date}\n\n\n')
	response.writelines(lines)
	return response
    
"""
def card_description(request, card_id):
    response = HttpResponse(content_type='text/plain')
    response["Content-Disposition"] = "attachment; filename=description.txt"
    card_des = Card.objects.get(pk=card_id)
    lines = []
    for card in card_des:
        lines.append(f'{card.description}')
    response.writelines(lines)
    return response"""

def card_full_text(request, card_id):
    card = Card.objects.get(pk=card_id)
    return render(request, 'main/card_full_text.html', {"card":card, "title":"Полный текст постановления", })
    _
def edit(request, card_id):
    card = Card.objects.get(pk=card_id)
    form = CardForm(request.POST or None, instance=card)
    if form.is_valid():
        form.save()
        return redirect('main:home')
    return render(request, 'main/edit.html', {'card':card, 'title':'Редактирование карточки',  'form':form,})

def delete(request,card_id):
    card = Card.objects.get(pk=card_id)
    card.delete()
    return redirect('main:home')


def rights(request):
    cards = Card.objects.all().order_by('date')
    return render(request, "main/rights.html", {"title":"Постановления", "cards":cards})

def add_card(request):
    submitted = False 
    if request.method == "POST" :
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_card?submitted=True")
    else: 
        form = CardForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "main/add_card.html", {"title":"Добавление карточки", "form":form, "submitted":submitted})

