

################################################################################
#### Math Import ###############################################################
import math

from random import randint, uniform

#################################################################################
#### Sabit sayılar  #############################################################
print("PI: ",math.pi)
print("E: ",math.e)
print()


##########################################################################
#### Math İşlemler  ######################################################
print("Karekök: ",math.sqrt(16))
print("üslü-1: ",math.pow(2,5))
print("üslü-2: ",(2**5))

print("Floor: ",math.floor(4.9))
print("ceil: ",math.ceil(4.1))

print("faktöriyel: ",math.factorial(4))

print()

##########################################################################
#### Aggreate Function####################################################
number1=[1,2,3,4,5,6]

print("Max: ", max(number1))
print("Min: ", min(number1))
print("Sum: ", sum(number1))
print("Average: ", sum(number1)/len(number1))

print()

##########################################################################
#### Random Function##################################################
print("Rastgele sayılar: ",randint(1,100))
print("Ondalıklı sayılar: ",uniform(0,1))

print()
##########################################################################
#### Logaritmik Function##################################################
print("Logaritma", math.log(100))
print("Sinüs", math.sin(90))
print("Cosinüs", math.cos(90))
print("Radyan", math.radians(90))
print("Derece", math.degrees(math.pi/2))


