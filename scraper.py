import requests
import math
import time
import random
import datetime
import os
import pickle

ROOT_URL = 'https://d3e6htiiul5ek9.cloudfront.net/prod/'
STORES = 'sucursales'
PRODUCTS = 'productos'
STORES_PARAMS = params = {'lat': -34.60028000712061, 'lng': -58.44062160732691, 'limit': 30}
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_available_stores(offset=0, headers=HEADERS, params=STORES_PARAMS, total=int(math.exp(99))):

	print('Getting stores:', offset)
	stores = []
	if offset <= total:
		time.sleep(random.random())
		params['offset'] = offset
		r = requests.get(ROOT_URL+STORES, params=params, headers=headers)
		j = r.json()
		stores = j['sucursales'] + get_available_stores(offset=offset+30, total=j['total'])
	return stores

def get_products(store_id, offset=0, headers=HEADERS, total=int(math.exp(99))):
	
	products = []
	if offset <= total:
		time.sleep(random.random())
		params = {
			'array_sucursales': store_id,
			'offset': offset,
			'limit': 100
		}
		r = requests.get(ROOT_URL+PRODUCTS, params=params, headers=headers)
		j = r.json()
		print('Got',min(offset+100,j['total']),'of',j['total'],'products in store',store_id)
		products = j['productos'] + get_products(store_id, offset=offset+100, total=j['total'])
	return products

def store_data(data, filename):
	date = datetime.datetime.now().strftime('%Y-%m-%d')
	dir_path = os.path.join('data',date)
	os.makedirs(dir_path, exist_ok=True)
	file_path = os.path.join(dir_path,filename+'.pickle')
	with open('filename.pickle', 'wb') as handle:
		pickle.dump(data, handle)


def main():

	success = False
	while not success:
		print('Getting available stores...')
		try:
			stores = get_available_stores()
			while len(stores) > 0:
				random.shuffle(stores)
				try:
					products = get_products(stores[0]['id'])
					store_data(products, stores[0]['id'])
					del stores[0]
				except:
					print('Request unsuccessful for store',stores[0]['id'],'Retrying another store in 1 minute.')
					time.sleep(60)
			success = True
		except:
			print('Request unsuccessful. Retrying in 1 minute.')
			time.sleep(60)


if __name__ == '__main__':
	main()
	