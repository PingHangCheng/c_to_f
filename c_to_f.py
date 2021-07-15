#溫度轉換程式
#使用輸入攝氏溫度
#印出華氏溫度
C = input('請輸入攝氏溫度: ')
C = float(C)
F = C * 9 / 5 + 32
print ('華氏溫度為: ', F ) #兩者合併用 , 
price = 100
pen = 9.6
rain = True
name = 'John'
print(price, pen, rain, name) #練習合併用 ,

F1 = input('請輸入華氏溫度: ')
F1 = float(F1)
C1 = (F1 - 32) * 5 / 9
print ('攝氏溫度為: ', C1 )  