import easytrader

user = easytrader.use('ht_client')

try:
	user.prepare(user='666637575127', password='671109', comm_password='671109')
except:
	pass

user.cancel_entrust('20615')

print(user.balance)
print(user.position)