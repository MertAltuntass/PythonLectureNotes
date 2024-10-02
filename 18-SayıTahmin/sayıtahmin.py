import random

secret_number = random.randint(1, 100)  # Rastgele bir sayı seçme
guess = None  # İlk başta guess değişkenini tanımlıyoruz

while guess != secret_number:  # Kullanıcı doğru tahmin edene kadar devam et
    guess = int(input("Tahmin ediniz: "))  # Kullanıcıdan tahmin alma

    if guess < secret_number:
        print("Daha büyük bir sayı dene!")
    elif guess > secret_number:
        print("Daha küçük bir sayı dene!")
    else:
        print("Bildiniz!")  # Kullanıcı doğru tahmin yaptığında

        