#----------------- Serie 1 ex 01 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = input("Entrez une valeur :")
positif = 0
negative = 0

for i in range(0, n):
    if float(t[i]) >= 0:
        positif +=1
    else:
        negative += 1


print("le nombre de valeur positif :", positif)
print("le  nombre de valeur negatif :", negative)      

'''

#----------------- Serie 1 ex 02 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = float(input("Entrez une valeur :"))
pair = 0
impair = 0

for i in range(0, n):
    if int(t[i]) % 2 == 0:
        pair +=1
    else:
        impair += 1

print("le nombre de valeur pair :", pair)
print("le nombre de valuer impair :", impair)        


'''


#----------------- Serie 1 ex 03 --------------------

'''
n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = float(input("Entrez une valeur :"))

for i in range(0, n):
    if t[i] < 0:
        t[i] = -t[i]


print(*t)        

'''

#----------------- Serie 1 ex 04 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
somme = 0
for i in range(0, n):
    t[i]  = float(input("Entrez une valeur :"))
    somme += t[i]

supp = 0
infr = 0
moyenne = somme / n
for i in range(0, n):
    if t[i] > moyenne:
        supp += 1
    elif t[i] < moyenne:
        infr += 1


print("La valeur moyenne", moyenne)
print("Le nombre de valeur suppérior à la valeur moyenne", supp)
print("Le nombre de valeur inférior à la valeur moyenne", infr)            


'''

#----------------- Serie 1 ex 05 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = float(input("Entrez une valeur :"))

maxv = max(t)
minv = min(t)

print("La valeur maximale :", maxv)
print("la valeur minimale :", minv)  

'''


#----------------- Serie 1 ex 07 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = input("Entrez une valeur :")

#l.sort()

while sorted(t) != t:
    for i in range(0, n-1):
        if t[i] > t[i+1]:
            t[i] , t[i+1] = t[i+1] , t[i]

print("le tableau ordonné :",*t)

'''

#----------------- Serie 1 ex 08 --------------------

'''
n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = input("Entrez une valeur :")
index = n
for i in range(0, n//2):
    index -= 1
    if t[i] != t[index]:
        
        t[i] , t[index] = t[index] , t[i]

print("Son inverse :", *t)

'''



#----------------- Serie 1 ex 09 --------------------


'''
n = int(input("Entrez une valeur :"))
temp = n
t = []

while n != 0:
    w = n % 2
    t.append(w)
    n //= 2

    

t.reverse()
print(f"la base binaire de {temp} est :", ''.join(str(i) for i in t))    

'''

#----------------- Serie 1 ex 10 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = input("Donner une valeur :")

x, position = input("entrer une valeur à ajouter") , int(input("et sa position sur le tableau")) 

t.insert(position, x)
print(*t)

'''