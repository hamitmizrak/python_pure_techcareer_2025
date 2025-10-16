#### 1- (for veya while), break, continue, pass ###############################
# step-1) 1-10 arasındaki sayıları verilsin
# step-2) Başlangıç ile bitiş sayıları arasında sayıların toplamını yapınız ?
# step-3) Eğer sayı eğer 10 sonra devam ediyorsa dur (döngüyü bitir) ?
# step-4) Eğer bu döngüdeki sayılarda 5 varsa işleme alma(toplama yapma) ?
# step-5) Eğer bu döngüdeki sayılarda 6 varsa bir şey yapma (pass'ı ekleyiniz) ?
# step-6) 1-10 arasındaki tek sayıları gösteriniz ve tek sayıları toplayınız ?
# step-7) 1-10 arasındaki çift sayıları gösteriniz ve çift sayıları toplayınız ?

# Global Variable
toplam=0
tek_toplam=0
cift_toplam=0
for temp in range(1,10000):    # Step-1 (1-10 arasında olacak ancak biz 10.000 verdik)
    if temp > 10:              # step-2 sayı>10 büyüksek dur
        break
    if temp==5:                # Step-3 sayı: 5 toplama
        continue
    if temp ==6:               # Step-4 sayı: 6 hiç birşey yapma
        pass
    toplam +=temp              # 5 hariç ve 1...10 kadar toplama yap

    # Tek işlemler
    tekler = [temp for temp in range(1, 11) if temp % 2 == 1 and temp!=5]
    tek_toplam = sum(tekler)

    # Çiftler işlemler
    ciftler = [temp for temp in range(1, 11) if temp % 2 == 0]
    cift_toplam = sum(ciftler)

print(f"Dikkat: 5 hariç ve 1...10 kadar toplama")
print(f"{toplam}")
# 1 2 3 4 5 6 7 8 9 10 = 55-5=50

print(f" Tek sayılar {tekler}")
print(f" Tek sayılar toplamı {tek_toplam}\n")

print(f" Çift sayılar {ciftler}")
print(f" Çift sayılar toplamı {cift_toplam}")



################################################################################
#### 2- (for veya while), break, continue, pass ################################
# step-1) kullanıcı tarafından başlangıç ve bitiş sayıları verilsin
# step-2) Başlangıç ile bitiş sayıları arasında sayıların toplamını yapınız ?
# step-3) Eğer sayı eğer 10 sonra devam ediyorsa dur (döngüyü bitir) ?
# step-4) Eğer bu döngüdeki sayılarda 5 varsa işleme alma(toplama yapma) ?
# step-5) Eğer bu döngüdeki sayılarda 6 varsa bir şey yapma (pass'ı ekleyiniz) ?
# step-6) 1-10 arasındaki tek sayıları gösteriniz ve tek sayıları toplayınız ?
# step-7) 1-10 arasındaki çift sayıları gösteriniz ve çift sayıları toplayınız ?