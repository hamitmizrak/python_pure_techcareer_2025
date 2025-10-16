################################################################################
#### Loop        ###############################################################

#### Loop Over   ###############################################################
my_list  = [1,2,3,4,5,6,7,8,9]  # list
for temp in my_list:
    print(f"{temp} ",end=" ")
print("\n*********************************")

#### Range  ###############################################################
# range() =>= fonksiyonu belirli aralıktaki sayıları üretmek için kullanıyoruz
for temp in range(10):  # 0<=sayı<10
    print(f"{temp} ",end=" ")
print("\n*********************************")

#### Range  #####################################################################
# range() =>= fonksiyonu belirli aralıktaki sayıları üretmek için kullanıyoruz
# range(start,stop)
# range(start,stop, step)
for temp in range(1,10,2):  # 0<=sayı<10
    print(f"{temp} ",end=" ")

print("\n*********************************")
#### Örnek  ######################################################################
# 10'a kadar (10 dahil) olan sayıların toplamını veren örnek
#1.YOL
sum_data1=sum(range(1,11))
print(f"1-10 toplamı:  {sum_data1}")
print("\n*********************************")


#2.YOL
sum_data2=0
for temp in range(11):   #range(1,11):
    sum_data2=sum_data2+temp
    print(f"1-10 toplamı:  {sum_data2}")
print(f"1-10 toplamı:  {sum_data2}")

print("\n******while***************************")
################################################################################
#### while  ####################################################################
data:int=0
while data<5:
    print(data) # sonsuz döngüdür dikkat
    data += 1

################################################################################
#### (for veya while), break, continue, pass ###################################
# step-1) 1-10 arasında sayıların toplamını yapınız ?
# step-2) Eğer sayı eğer 10 sonra devam ediyorsa dur (döngüyü bitir) ?
# step-3) Eğer bu döngüdeki sayılarda 5 varsa işleme alma(toplama yapma) ?
# step-4) Eğer bu döngüdeki sayılarda 6 varsa bir şey yapma (pass'ı ekleyiniz) ?
# step-5) 1-10 arasındaki tek sayıları gösteriniz ve tek sayıları toplayınız ?
# step-6) 1-10 arasındaki çift sayıları gösteriniz ve çift sayıları toplayınız ?
