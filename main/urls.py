from django.urls import path 
from . import views 
from django.views.i18n import JavaScriptCatalog

app_name = 'main'
urlpatterns = [
    path('', views.index, name="home"), 
    path("rights/", views.rights, name="rights"),
    path("add_card", views.add_card, name="add-card"),
    path("show_card/<card_id>", views.show_card, name="show-card"), 
    path('search', views.search, name="search"),
    path('edit/<card_id>', views.edit, name="edit"), 
    path('delete/<card_id>', views.delete, name="delete"),
    path('card_text', views.card_text, name='card_text'),
    path('card_full_text/<card_id>', views.card_full_text, name="card_full_text"),
] 

"""    path('card_description/<card_id>', views.card_description, name="card_description"),"""