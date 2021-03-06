
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

    try:
        result['type']=jw['object_type'].capitalize()
    except:
        result['type']='Default'

    try:
        result['desc']=jw['short_description']
    except:
        result['desc']='Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
        Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,\
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.'

    try:
        result['title']=jw['title']
    except:
        result['title']='Default'

    try:
        result['lang']=lang.get(jw['original_language'], jw['original_language'].capitalize())
    except:
        result['lang']='Default'

    try:
        result['year']=jw['original_release_year']
    except:
        result['year']='Default'

    try:
        result['tmdb']=round(jw['tmdb_popularity'],2)
    except:
        result['tmdb']='Default'

    try:
        result['poster']=base_url + jw['poster'].split('{')[0] + poster_size
    except:
        result['poster']='https://namotreks.com/wp-content/themes/himalayanbuddha/img/default.png'

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
    