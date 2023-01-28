#----------------- Serie 1 ex 01 --------------------

'''

n = int(input("Donner le nombre de cas :"))
t = [None] * n
for i in range(0, n):
    t[i]  = int(input("Donner un entier :"))
positif = 0
negative = 0

for i in range(0, n):
    if t[i] >= 0:
        positif +=1
    else:
        negative += 1


print("le nombre de valeur positif :", positif)
print("le  nombre de valeur negatif :", negative)      

'''