nameDictionary = {}
f = open('./namen.txt', "r")

if f.mode == 'r':
	names = f.read().splitlines()
	print(names)

	for name in names:
		if name not in nameDictionary:
			nameDictionary[name] = 1
		else: 
			nameDictionary[name] += 1

	for name in nameDictionary:
		print(name, end=': ')
		print(nameDictionary[name])
