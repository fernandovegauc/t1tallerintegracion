from django.shortcuts import render
import requests
from .services import get_seasons, get_episodes_BB, get_episodes_BCS, get_info_episode, get_info_character, get_info_quote, search_character
# Create your views here.
def index(request):
    """View function for home page of site."""

 

    context = {'seasons_BCS': get_seasons('Better+Call+Saul'),
        'seasons_BB': get_seasons('Breaking+Bad')
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def season(request,serie, season):
    """View function for seasons page of site."""

 

    context = {'episodes_BB': get_episodes_BB(str(season)),
    'episodes_BCS': get_episodes_BCS(str(season)),
    'season': season,
    'serie': serie
    
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'seasons.html', context=context)
def episodes(request,season, serie, episode):
    """View function for seasons page of site."""

 

    context = {'episode': episode,
    'season': season,
    'serie': serie,
    'info': get_info_episode(serie, season, episode)
    
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'episodes.html', context=context)
'''
def characters(request,season, serie, episode, character):

    context = {'character_info': get_info_character(character),
    'quote_info': get_info_quote(character),
    'episode': episode,
    'season': season,
    'serie': serie
    

    }


    return render(request, 'characters.html', context=context)
'''

def search(request):
    context = {'search_character': search_character(request.GET.get('SearchValue'))

    }

    return render(request, 'search.html', context=context)

def search_s(request,season):
    context = {'search_character': search_character(request.GET.get('SearchValue'))

    }

    return render(request, 'search.html', context=context)


def characters(request, character):

    context = {'character_info': get_info_character(character),
    
    

    }
    return render(request, 'character_new.html', context=context)

