from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('<str:character>', views.characters, name='characters'),
    
   # path('character_new.html/<str:character>', views.characters_new, name='character_new'),

    

    
    
    path('seasons/<int:season>/<str:serie>', views.season, name='seasons'),
    path('seasons/<int:season>/<str:serie>/<str:episode>', views.episodes, name='episodes'),
    path('/<str:character>', views.characters, name='characters'),


   
]