#----------------- Serie 1 ex 01 --------------------
'''

n = 0
while n >= 0:
    n = int(input("Donner un entier :"))

'''
#----------------- Serie 1 ex 02 --------------------
'''

n = int(input("Donner un entier entre 0 et 20 :"))

while n < 0 or n > 20:
    n = int(input("Donner un entier entre 0 et 20 :"))


'''

#----------------- Serie 1 ex 03 --------------------

'''

n = 1
c = 0
s = 0
while n != 0:
    
    n = int(input("Donner un entier, (entre 0 pour sortir) :"))
    if n == 0: break
    c+=1
    s = s + n

moy = s / c
print("La valeur moyenne est :", moy)


'''


#----------------- Serie 1 ex 04 --------------------

'''
n = int(input("Donner un entier, (entre 0 pour sortir) :"))
maxv = n
minv = n



while n != 0:
    
    n = int(input("Donner un entier, (entre 0 pour sortir) :"))
    if n == 0: break

    if n > maxv:
        maxv = n
    elif n < minv:
        minv = n
    

print("La valeur maximal est : ", maxv)   
print("La valeur minimal est : ", minv)

'''

#----------------- Serie 1 ex 05 --------------------

'''

n = int(input("Donner un entier, (entre 0 pour sortir) :"))
minv = n
counter = 1

while n != 0:

    n = int(input("Donner un entier, (entre 0 pour sortir) :"))
    if n == 0: break

    if n < minv:
        minv = n
        counter = 1
    elif n == minv:
        counter += 1

print("La valeur minimal est : ", minv)
print("Son nomber d'occurence", counter)    


'''


#--------------------- Serie 1 ex 06 -----------------------

'''


n = int(input("Donner un entier postive, (entre un valeur negatif pour soritr) :"))
maxv = n
Poccu = Doccu = 1
counter = 1



while n >= 0:
    n = int(input("Donner un entier postive, (entre un valeur negatif pour sortir) :"))
    if n < 0: break
    counter += 1

    if n > maxv:
        maxv = n
        Poccu = Doccu = counter
        
    elif n == maxv:
        Doccu = counter


print("La valeur maximal est : ", maxv)
print("Sa premier occcurence : ", Poccu)
print("Sa dernier occurence :", Doccu)

'''


#--------------------- Serie 1 ex 07 -----------------------

'''

n = int(input("Donner un entier postive, (entre un valeur negatif pour sortir) :"))


maxv = n
Poccu = Doccu = 1
somme = n
counter = 1
nombreOccu = 1


while n != 0:
    n = int(input("Donner un entier postive, (entre un valeur negatif pour sortir) :"))
    if n == 0: break
    somme = somme + n
    counter += 1

    if n > maxv:
        maxv = n
        Poccu = Doccu = counter
        nombreOccu = 1
    elif n == maxv:
        Doccu = counter
        nombreOccu += 1

moyenne = somme / counter


print("La somme des valeurs :", somme)
print("le nombre de valeurs saise :", counter)
print("la valeur moyenne :", moyenne)
print("La valeur maximal est : ", maxv)
print("Sa premier occcurence : ", Poccu)
print("Sa dernier occurence :", Doccu)
print("nombre d'occurence :", nombreOccu)



'''