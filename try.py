portfolio = []
while True:
    stock = {}
    tmp = input()
    if tmp == 'quit':
        break
    stock['symbol'] = tmp
    name = input()
    stock['name'] = name
    portfolio.append(stock)
    print(stock['symbol'], stock['name'])
    print(portfolio)
    print("%s (%s) has a value" %(stock['name'], stock['symbol']))
 
while True:
	tmp = input()
	for i in portfolio:
		if(i['symbol'] == tmp):
			print(i['name'])

