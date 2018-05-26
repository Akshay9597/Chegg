import random
a={}
sum = 0
for j in range(10000):
	for i in range(1,366):
		a[i] = 0
	flag = 1
	count = 0
	while flag:
		t = (random.randint(1,365))
		a[t] = a[t] + 1
		for k,v in a.items():
			if(v == 3):
				flag = 0
				break
		count += 1
	sum = sum + count
print(sum / 10000)
