#讀取檔案
import os #operating system
products = []
if os.path.isfile('products.csv'):#相對路徑
	print('我找到檔案了')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f :
			if '產品,價格' in line:
				continue #這一行不處理，跳到下一行 
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('找不到檔案')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	price = int(price)#將字串轉成整數
	products.append([name, price])
print(products) 

#印出所有購買紀錄
for p in products:#p是指小清單
	print(p[0], '的價格是', p[1])#小清單中商品名稱的價格

#寫入檔案
with open ('products.csv', 'w', encoding = 'utf-8')as f:#打開檔案，就算該檔案不存在，仍會重寫覆蓋出來
	f.write('產品,價格\n')#標題列
	for p in products:
		f.write(p[0] + ',' + str(p[1] )+ '\n')#字串用+號來合併，最後換行符號，真正的寫入,將價格整數轉換成字串再合併

