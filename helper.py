
providers={
            2: {'link': '/icon/430995/', 'name': 'Apple iTunes'},
            3: {'link': '/icon/430996/', 'name': 'Google Play Movies'},
            8: {'link': '/icon/430997/', 'name': 'Netflix'},
            11: {'link': '/icon/438826/', 'name': 'Mubi'},
            73: {'link': '/icon/104966985/', 'name': 'Tubi TV'},
            100: {'link': '/icon/2625277/', 'name': 'GuideDoc'},
            119: {'link': '/icon/52449861/', 'name': 'Amazon Prime Video'},
            121: {'link': '/icon/4233119/', 'name': 'Voot'},
            122: {'link': '/icon/4233120/', 'name': 'Hotstar'},
            124: {'link': '/icon/4302033/', 'name': 'Bookmyshow'},
            125: {'link': '/icon/4304905/', 'name': 'Hooq'},
            158: {'link': '/icon/6918774/', 'name': 'Viu'},
            175: {'link': '/icon/14385750/', 'name': 'Netflix Kids'},
            192: {'link': '/icon/59562423/', 'name': 'YouTube'},
            218: {'link': '/icon/82869265/', 'name': 'Eros Now'},
            220: {'link': '/icon/85114140/', 'name': 'Jio Cinema'},
            232: {'link': '/icon/93795879/', 'name': 'Zee5'},
            237: {'link': '/icon/99832956/', 'name': 'Sony Liv'},
            255: {'link': '/icon/123324312/', 'name': 'Yupp TV'},
            283: {'link': '/icon/127445869/', 'name': 'Crunchyroll'},
            309: {'link': '/icon/138047862/', 'name': 'Sun Nxt'},
            315: {'link': '/icon/141253805/', 'name': 'Hoichoi'},
            319: {'link': '/icon/141488812/', 'name': 'Alt Balaji'}
        }

lang={
    
    'en':'English',
    'hi':'Hindi',
    'pa':'Punjabi',
    'mr':'Marathi',
    'gu':'Gujarati',
    'ta':'Tamil',
    'te':'Telugu'
}

base_url='https://images.justwatch.com'
poster_size='s592'
icon_size='s100'

from justwatch import JustWatch

justwatch = JustWatch(country='IN')

def createResponse(query):
    result={}
    jwresponse=justwatch.search_for_item(query=query)
    
    if not len(jwresponse['items']):
        return result
    
    jw=jwresponse['items'][0]
    result['type']=jw['object_type'].capitalize()
    result['desc']=jw['short_description']
    result['title']=jw['title']
    result['lang']=lang[jw['original_language']]
    result['year']=jw['original_release_year']
    result['tmdb']=round(jw['tmdb_popularity'],2)
    result['poster']=base_url + jw['poster'].split('{')[0] + poster_size
    provider_list=[]

    if 'offers' in jw:
        offers=jw['offers']
        provider_id=[]
        
        for offer in offers:
            if offer['provider_id'] not in provider_id:
                id=offer['provider_id']
                provider={}
                provider_id.append(id)
                provider['name']=providers[id]['name']
                provider['icon']=base_url + providers[id]['link'] + icon_size
                provider['link']=offer['urls']['standard_web']
                provider_list.append(provider)

    result['providers']=provider_list    
            
    for score in jw['scoring']:
        if score['provider_type']=='imdb:score':
            result['imdb']=score['value']
            break
    
    
    return result

def getImageLinks():
    
    jw = JustWatch(country='IN',genres=['act', 'scf', 'com'])
    results = jw.search_for_item()['items'][:5]
    resultsArr=[]
    for item in results:
        resultsArr.append({
            'title':item['title'],
            'poster':base_url + item['poster'].split('{')[0] + poster_size
        })
    
    return resultsArr
    