
# Register your models here.
from django.contrib import admin
from .models import Card, FirstDispute


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "case_number", "trial", "documents", "instance", "intial", "counter", "appellate", "cassation", "second1_dispute","second2_dispute", "third_dispute", "proceeding", "review", "motivation", )
    search_fields = ("name", "date", "case_number", "trial", "second1_dispute", "second2_dispute",  "third_dispute",)
    fields = (("name", "trial"),  "instance", ("intial", "counter"), "appellate", "cassation", ("first_dispute","second1_dispute", "second2_dispute",  "third_dispute"), "proceeding",  ("review","motivation"), ("case_number", "description"), "documents", "date",)
    list_filter = ('date', 'trial', 'instance',)
    filter_horizontal = ("first_dispute",)


@admin.register(FirstDispute)
class FirstDisputeCard(admin.ModelAdmin):
    list_display = ("value",)
   
    