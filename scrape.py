import datetime
import pandas as pd
import requests
import time

def scrape(interval):
	
	targets = [
			'160325',
			'160926',
			'501080',
			'501082',
			'506002',
			'506003',
			'506006'
		]
	
	log_df = pd.DataFrame()
	
	dt = datetime.datetime.now()
	
	while dt.time() < datetime.time(11, 30):
	
		print(dt.time())
		now = datetime.datetime.now()

		snapshot = {now : {}}
		for code in targets:
			
			headers = {
				'content-type': 'application/json',
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
			}
			
			response = requests.get(f'https://fundgz.1234567.com.cn/js/{code}.js', headers=headers)
			NAV = float(eval(response.text.replace('jsonpgz(', '').replace(');', ''))['gsz'])
			
			snapshot[now][code + ' NAV'] = NAV
		
		dt = datetime.datetime.now()
		
		log_df = pd.concat([log_df, pd.DataFrame(snapshot).T], axis=0)
	
		time.sleep(interval)
		
	return log_df


if __name__ == '__main__':

	log_df = scrape(60)

	log_df.to_csv('test.csv')
