print("Merhaba 2 adet sayı giriniz: ")
sayı1 = int(input("Sayı 1 giriniz: "))
sayı2 = int(input("Sayı 2 giriniz: "))

print("Hangi matematiksel işlemi yapmak istersiniz? 1-Toplama 2-Çıkarma 3-Çarpma 4-Bölme")
islem = int(input("Yapmak istediğiniz işlem numarasını giriniz: "))

if islem == 1:
	toplama = sayı1 + sayı2
	print(toplama)
elif islem == 2:
	cıkarma = sayı1 - sayı2 
	print(cıkarma)
elif islem == 3:
	carpma = sayı1 * sayı2 
	print(carpma)
elif islem == 4:
	
	if sayı2 == 0:
		print()
	else:
		bölme = sayı1 / sayı2
		print(bölme)
else:
	print("Geçersiz bir işlem numarası girdiniz 1 ~ 2 ~ 3 ~ 4 rakamlarını kullanınız!")