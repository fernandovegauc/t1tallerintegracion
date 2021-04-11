import requests
## code based on https://codigofacilito.com/articulos/consumir-api-django

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_seasons(params={}):
    response = generate_request('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=' + params, params)
    seasons = []
    for episode in response:
        if not episode['season'] in seasons:
            seasons.append(episode['season'])       
    return seasons

def get_episodes_BB(params={}):
    response = generate_request('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad', params)
    episodes = []
    for episode in response:
        if episode['season'] == str(params):
            episodes.append(episode['title'])       
    return episodes

def get_episodes_BCS(params={}):
    response = generate_request('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul', params)
    episodes = []
    for episode in response:
        if episode['season'] == str(params):
            episodes.append(episode['title'])       
    return episodes

def get_info_episode(serie, season, episode):
    if serie == 'BB':
        response = generate_request('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    else:
        response = generate_request('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    
    
    for epi in response:
        if epi['title'] == episode and epi['season'] == str(season):
            response = epi



  
    return response

def get_info_character(character):
    
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters' 
    params = {'name': character}
    response = generate_request(url, params)
    
    if response:
        return response[0]
    return

def get_info_quote(character):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote' 
    params = {'author': character}
    response = generate_request(url, params)

    
    
    return response  
    
   
def search_character(SearchValue):
    offset = 0
    json_global = []
   
    while 1:
        url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters' 
        params = {'name': SearchValue, 'offset':offset}
        response = generate_request(url, params)
        if  len(response) == 0:
            break
        else:
            offset += 10
            json_global += response


    

    return json_global
        

