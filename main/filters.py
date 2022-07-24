import django_filters
from django_filters import DateFilter
from .models import *
from django import forms 



class CardFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte', label="Дата вынесения с",  widget=forms.DateInput(attrs={'class': 'form-control', 'style': 'width:400px'}))
    end_date = DateFilter(field_name="date", lookup_expr='lte', label="по",  widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px'}))
    case_number = django_filters.CharFilter(lookup_expr='iexact', label="Номер дела", widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px'}))
    proceeding = django_filters.MultipleChoiceFilter(choices=Card.PROCEEDING_CHOICES, label="Вид судопроизводства (выберите подходящее значение)", widget=forms.SelectMultiple(attrs={'class':'form-control', 'style': 'width:400px'}))
    trial = django_filters.MultipleChoiceFilter(choices=Card.TRIALS,label="Наименование суда (выберите подходящее значение)", widget=forms.SelectMultiple(attrs={'class':'form-control', 'style': 'width:400px' }))
    first_dispute = django_filters.MultipleChoiceFilter(choices=FirstDispute.CHOICES, label="Первая категория спора (выберите подходящее значение)", widget=forms.SelectMultiple(attrs={'class':'form-control', 'style': 'width:400px' }))
    class Meta: 
        model = Card
        fields = ['proceeding', 'trial', 'case_number', 'first_dispute']
