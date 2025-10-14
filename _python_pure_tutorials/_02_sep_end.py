

#################################################################################
####### docstring ###############################################################

# Buradaki """ ile alt satırdaki sırada veriler gelir
print("""1.satır
2.satır
3.satır
""")


#################################################################################
####### seperate ################################################################

# sep: Veriler arasında nasış bir karakter olsun.
# Dikkat: Veriler arasında istediğimiz karakterin gelmesi için örneğin: (*) kullanıyoruz.
print("Merhabalar", "Python", "Öğreniyorum", sep=" - ")


#################################################################################
####### end #####################################################################

# end parametresi yeni bir satıra geçmesini engellemek yani aynı satırda devam etmek istiyorsak
print("1- Merhabalar", "Python", "Öğreniyorum", " Data Science", "Python dünyası"," Machine Learning",)

# Python kodlarda ki Okumayı daha iyi artırmak için end="" kullanıyoruz.
print("2- Merhabalar", "Python", "Öğreniyorum", end= " ")
print(" Data Science", "Python dünyası"," Machine Learning")