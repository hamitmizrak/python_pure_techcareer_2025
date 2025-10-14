#################################################################################
####### Variable(str) #########################################################
# 1.YOL ==> (Okunabilirliği(-), yazılabilirlik(-))
name="Hamit"
surname="Mızrak"
print("Adım: ", name, " Soyadım: ", surname)

#################################################################################
####### Formatter #########################################################
# 2.YOL  ==> Okunabilirliği(-), yazılabilirlik(+)
# s: string
# d: decimal
# f: float
print("Adım:  %s  Soyadım:  %s "%(name,surname))   # 2.YOL: Okunabilirliği(+)

# 3.YOL   ==> Okunabilirliği(-), yazılabilirlik(+)
# Python >=3.6
# dikkat: f anlamı formatter yani f-string
print(f"Adım:  {name}  Soyadım:  {surname}")   # 3.YOL: Okunabilirliği(+)

#################################################################################
####### Escape Character#########################################################
print("""1.satır
2.satır
3.satır
""")

# Escape : Çıkış karakter
print("""\n\r\t4.satır
5.satır
6.satır
""")
