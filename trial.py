import multiprocessing
from multiprocessing import Manager
import requests
import time

def foo(targets, return_ls):
	ans = []
	for target in targets:
		headers = {
				'content-type': 'application/json',
				'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
			}
		response = requests.get(f'https://fundgz.1234567.com.cn/js/{target}.js', headers=headers)
		NAV = float(eval(response.text.replace('jsonpgz(', '').replace(');', ''))['gsz'])
		ans.append(NAV)
		
		return_ls.append(ans)

def get(t):

	targets = [
		'506002',
		'501082',
		'506006',
		'160926',
		'506003',
		'160325',
		'501080'
	]

	manager = Manager()
	# return_list = manager.list() 也可以使用列表list
	return_ls = manager.list()

	p = multiprocessing.Process(target=foo, args=(targets,return_ls))
	p.start()
	time.sleep(t)
	p.terminate()
	p.join()

	return return_ls.
