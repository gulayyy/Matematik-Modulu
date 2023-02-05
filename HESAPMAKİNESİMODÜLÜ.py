import time
import math

while True:
    işlem = int(input("İşleminizi giriniz:"))
    if(işlem == "q"):
        print("Program sonlandırılıyor......")
        time.sleep(2)
        print("Tekrar Bekleriz....")
        break
    elif(işlem == 1):
        sayı1 = int(input("Sayı-1:"))
        sayı2 = int(input("Sayı-2:"))
        print("İşleminiz Yapılıyor....")
        time.sleep(1)
        print("{} + {} = {} ".format(sayı1,sayı2,(sayı1+sayı2))

    elif(işlem == 2):
        sayı1 = int(input("Sayı-1:"))
        sayı2 = int(input("Sayı-2:"))
        print("İşleminiz Yapılıyor....")
        time.sleep(1)
        print("{} - {} = {} ".format(sayı1,sayı2,(sayı1-sayı2))
    elif(işlem == 3):
        sayı1 = int(input("Sayı-1:"))
        sayı2 = int(input("Sayı-2:"))
        print("İşleminiz Yapılıyor....")
        time.sleep(1)
        print("{} x {} = {} ".format(sayı1,sayı2,(sayı1*sayı2))
    elif(işlem == 4):
        sayı1 = int(input("Sayı-1:"))
        sayı2 = int(input("Sayı-2:"))
        print("İşleminiz Yapılıyor....")
        time.sleep(1)
        print("{} / {} = {} ".format(sayı1,sayı2,(sayı1/sayı2))
   elif(işlem == 5):
       sayı1 = int(input("Taban değerini giriniz:"))
       sayı2 = int(input("Üs değerini giriniz:"))
       print("İşleminiz yapılıyor....")
       time.sleep(1)
       x = math.pow(sayı1,sayı2)
       print("{} üssü {} = {}".format(sayı1,sayı2,math.pow(sayı1,sayı2))
   elif(İşlem == 6):
       sayı1 = int(input("Karekökü alınacak sayıyı girin:"))
       print("İşleminiz Yapılıyor.....")
       time.sleep(1)
       print("{} sayısının karekökü : {}".format(sayı1,(math.sqrt(sayı1)))
   elif(İşlem == 7):
       sayı1 = int(input("Logaritması alınmak istenen sayıyı girin:"))
       print("İşleminiz yapılıyor....")
       time.sleep(1)
       print("{} sayısnın logaritması : {}".format(sayı1,(math.log(sayı1)))
   elif(İşlem == 8):
       sayı1 = int(input("Radyana çevirmek istediğiniz sayıyı girin:"))
       print("İşleminiz yapılıyor....")
       time.sleep(1)
       print("{} derece {} randyandır.".format(sayı1(math.degrees(sayı1)))
   elif(İşlem == 9):
       sayı1 = int(input("Dereceye çevirmek istediğiniz sayıyı girin:")
       print("İşleminiz yapılıyor....")
       time.sleep(1)
       print("{} radyan {} derecedir.".format(sayı1,(math.radians(sayı1)))
   elif(işlem  == 10):
        a = input(" Radyan için = R , derece için = D")
        if(a == "r" or a == "R"):
             sayı1 = int(input("sinüsü alınmasını istediğiniz sayıyı girin:")
             x = math.sin(sayı1)
             print("İşleminiz yapılıyor....")
             time.sleep(1)
             print("sin{} = {}".format(sayı1,x)
        elif(a == "D" or a == "d"):
            sayı1 = int(input("Sinüsü alınmasını istediğiniz dereceyi girin:")
            x = math.sin(sayı1)
            y = math.radians(x)
            print("İşleminiz yapılıyor....")
            time.sleep(1)
            print("sin {} = {} ".format(sayı1,y))
   elif(İşlem == 11):
       a = input(" Radyan için = R , derece için = D")
       if(a == "D" or  a == "d"):
            sayı1 = int(input("Cosinüsünü almak istediğiniz dereceyi girin:"))
            print("İşleminiz yapılıyor....")
            time.sleep(1)
            print("cos {} = {} ".format(sayı1,(math.cos(sayı1)))
       elif(a == "R" or a == "r"):
            sayı1 = int(input("Cosinüsünü almak istediğiniz değeri girin:"))
            x = math.cos(sayı1)
            y = math.degrees(x)
            print("İşleminiz yapılıyor....")
            time.sleep(1)
            print("cos {} = {} ".format(sayı1,y))
   elif(İşlem == 12):
       a = input(" Radyan için = R , derece için = D")
       if(a == "D" or  a == "d"):
           sayı1 = int(input(" Dereceyi giriniz : "))
           print("işleminiz yapılıyor...")
           time.sleep(1)
           print("tan {} = {} ".format(sayı1,math.tan(sayı1)))
       elif(a == "R" or a == "r"):
            sayı1 = int(input("Tanjantını almak istediğiniz değeri girin:"))
            x = math.tan(sayı1)
            y = math.degrees(x)
            print("İşleminiz yapılıyor....")
            time.sleep(1)
            print("tan {} = {} ".format(sayı1,y)) 
   elif(İşlem == 13):
        a= input(" Radyan için = R , derece için = D")
       if(a == "D" or  a == "d"):
           sayı1 = int(input(" Dereceyi giriniz : "))
           print("işleminiz yapılıyor...")
           time.sleep(1)
           x = math.cos(sayı1)/math.sin(sayı1)
           print("cot {} = {} ".format(sayı1,x))
       elif(a == "R" or a == "r"):
            sayı1 = int(input("Cotanjantını almak istediğiniz değeri girin:"))
            x = math.cos(sayı1)/math.sin(sayı1)
            y = math.degrees(x)
            print("İşleminiz yapılıyor....")
            time.sleep(1)
            print("cot {} = {} ".format(sayı1,y)) 
