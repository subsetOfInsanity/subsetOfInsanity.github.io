import pandas as pd
import googlemaps
import os
import time

def get_city_coordinates(city):
    return gmaps.places(city)['results'][0]['geometry']['location']

def get_search_results(search: str, gmaps) -> pd.DataFrame:
    df_all = pd.DataFrame()
    stores = []
    page_token = None
    while True:
        result = gmaps.places(search) if not page_token else gmaps.places(search, page_token=page_token)
        df_results = pd.json_normalize(result['results'])
        df_all = df_all.append(df_results, ignore_index=True)
        page_token = result['next_page_token'] if 'next_page_token' in result else None
        if not page_token:
            return df_all
        time.sleep(2)

api_key = os.environ['GMAPS_API_KEY']

gmaps = googlemaps.Client(key=api_key)

city = 'Bern'
retailers = ['Migros', 'Coop', 'Lidl', 'Aldi']

df = pd.DataFrame()
for retailer in retailers:
    df_retailer = get_search_results('%s, %s' % (retailer, city), gmaps)
    df_retailer['retailer'] = retailer
    df = df.append(df_retailer)
    
df.to_csv('data/stores.csv', sep='\t', index=False)
