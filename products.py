products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	price = int(price)#將字串轉成整數
	products.append([name, price])
print(products) 

for p in products:#p是指小清單
	print(p[0], '的價格是', p[1])#小清單中商品名稱的價格


with open ('products.csv', 'w')as f:#打開檔案，就算該檔案不存在，仍會重寫覆蓋出來
	for p in products:
		f.write(p[0] + ',' + str(p[1] )+ '\n')#字串用+號來合併，最後換行符號，真正的寫入,將價格整數轉換成字串再合併

