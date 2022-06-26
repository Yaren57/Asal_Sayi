sayi = int(input("Asal olup olmadığını görmek için bir sayı giriniz: "))
if sayi > 1:
    for i in range(2, sayi):
        if (sayi % i) == 0:
            print("Sayı asal değildir. ")
            break
    else:
        print("Sayı asaldır. ")

else:
    print("Sayı asal değildir. ")