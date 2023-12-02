products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])
print(products) 

for p in products:#p是指小清單
	print(p[0], '的價格是', p[1])#小清單中商品名稱的價格是
