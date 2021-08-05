import requests
import time
from datetime import datetime
import pandas as pd

class stream:

	def __init__(self, code):

		self.code = code
		self.url = f'https://fundgz.1234567.com.cn/js/{code}.js'
		self.data = dict()
		self.df = pd.DataFrame()

	def get_evaluation(self):

		headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

		response = requests.get(self.url, headers=headers)
		data =eval(response.text.replace('jsonpgz(', '').replace(');', ''))

		print(data)

		self.data[datetime.now()] = eval(data['gsz'])

	def get_url(self):

		return self.url

	def to_df(self):

		self.df = pd.DataFrame(self.data.values(), index=self.data.keys(), columns=[f'{self.code} NAV'])

		print(self.df)