from django import forms 
from django.forms import ModelForm
from .models import Card, FirstDispute
import datetime

class FirstDispute(ModelForm):
    first_dispute = forms.MultipleChoiceField(choices=FirstDispute.CHOICES, label="Категория спора (подкатегория 1)", widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}), required=True)
    class Meta:
        model = FirstDispute
        fields = ('value',)

class CardForm(ModelForm):
    cur_year = datetime.datetime.today().year
    year_range = tuple([i for i in range(cur_year - 31, cur_year + 2)])
    instance = forms.ChoiceField(choices=Card.INSTANCE_CHOICES,  label="Инстанция (выберите подходящее значение)", initial='', widget=forms.Select(attrs={'class':'form-control',}), required=True)
    intial = forms.ChoiceField(choices=Card.REQUIREMENTS, label="Первоначальное решение первой инстанции", widget=forms.Select(attrs={'class':'form-control'}), required=False)
    counter = forms.ChoiceField(choices=Card.REQUIREMENTS, label="Встречное решение первой инстанции", widget=forms.Select(attrs={'class':'form-control'}), required=False)
    appellate = forms.ChoiceField(choices=Card.CHOICES, label="Решение апеляционной инстанции", widget=forms.Select(attrs={'class':'form-control'}), required=False)
    cassation = forms.ChoiceField(choices=Card.CHOICES, label="Решение кассационной инстанции", widget=forms.Select(attrs={'class':'form-control'}), required=False)
    trial = forms.ChoiceField(choices=Card.TRIALS, label="Наименование суда (выберите подходящее значение)", widget=forms.Select(attrs={'class':'form-control', }), required=True)
    proceeding = forms.ChoiceField(choices=Card.PROCEEDING_CHOICES, label="Вид судопроизводства (выберите подходящее значение)", widget=forms.Select(attrs={'class':'form-control', }), required=False)
    motivation = forms.ChoiceField(choices=Card.YES_OR_NO_CHOICES, label="Наличие мотивировочной части", widget=forms.RadioSelect, required=False)
    review = forms.ChoiceField(choices=Card.YES_OR_NO_CHOICES, label="Наличие истории рассмотрения", widget=forms.RadioSelect, required=False)
    second1_dispute = forms.ChoiceField(label="Категория спора (подкатегория 2-1)", choices=Card.SECOND1_DISPUTE, widget=forms.Select(attrs={'class':'form-control'}), required=False)
    second2_dispute = forms.ChoiceField(label="Категория спора (подкатегория 2-2)",choices=Card.SECOND2_DISPUTE, widget=forms.Select(attrs={'class':'form-control'}), required=False)
    third_dispute = forms.ChoiceField(label="Категория спора (подкатегория 3)", choices=Card.THIRD_DISPUTE, widget=forms.Select(attrs={'class':'form-control'}), required=False)
    date = forms.DateField(label="Дата вынесения постановления:",initial=datetime.date.today() - datetime.timedelta(days=7),widget=forms.SelectDateWidget(years=year_range), required=True)
    class Meta: 
        model = Card 
        fields = ("name", "trial",  "instance", "intial", "counter", "appellate", "cassation", "first_dispute", "second1_dispute", "second2_dispute", "third_dispute","proceeding", "motivation",  "review", "case_number", "description", "documents", "original_claim", "counter_claim", "date")
        labels = {
            'name': '',
            'trial': '', 
            'instance': '', 
            'intial':'', 
            'counter':'', 
            'appellate':'', 
            'cassation':'',
            'proceeding': '', 
            'first_dispute':'',
            'second1_dispute':'',
            'second2_dispute':'',
            'third_dispute':'',
            'motivation':'',
            'review': '', 
            'case_number': '', 
            'description':'Постановление',
            'documents':'',
            'original_claim':'Первоначальное требование',
            'counter_claim':'Встречное требование',
            'date':'', 
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':"Наименование постановления",}),
            'case_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Номер дела"}),
            'description':forms.Textarea(attrs={'class':'form-control', 'cols':60, 'rows':10,}),
            'documents':forms.Textarea(attrs={'cols':10, 'rows':5,'class':'form-control', 'placeholder':"Ссылки по сопутствущие документы", }),
            'original_claim':forms.Textarea(attrs={'cols':10, 'rows':3, 'class':'form-control',}),
            'counter_claim':forms.Textarea(attrs={'cols':10, 'rows':3, 'class':'form-control',}),
 
        }