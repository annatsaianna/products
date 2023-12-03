import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f :
            if '產品,價格' in line:
               continue #這一行不處理，跳到下一行 
            name, price = line.strip().split(',') #將1行的換行符號刪除及用逗號分開欄位
            products.append([name,price])
    return products


#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入價格: ')
        price = int(price)#將字串轉成整數
        products.append([name, price])
    print(products) 
    return products


#印出所有購買紀錄
def print_products(products):
    for p in products:#p是指小清單
        print(p[0], '的價格是', p[1])#小清單中商品名稱的價格


#寫入檔案
def write_file(filename, products):
    with open (filename, 'w', encoding = 'utf-8')as f:#打開檔案，就算該檔案不存在，仍會重寫覆蓋出來
        f.write('產品,價格\n')#標題列
        for p in products:
            f.write(p[0] + ',' + str(p[1] )+ '\n')#字串用+號來合併，最後換行符號，真正的寫入,將價格整數轉換成字串再合併


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#相對路徑,檢查檔案在不在資料夾裡
        print('找到檔案了')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()