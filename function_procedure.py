#----------------- Serie 1 ex 01 --------------------*


def remplir(t, n):
    for i in range(0, n):
        t.append(input(f"Denner la valeur {i+1} dans le tableu :"))
    



#----------------- Serie 1 ex 02 --------------------*


def trier(t):
    for i in range(0, len(t)):
        for j in range(0, len(t)-i-1):
            if t[j] > t[j + 1]:
                    t[j] , t[j+1] = t[j+1], t[j]




#----------------- Serie 1 ex 03 --------------------*


def afficher(t):
    for i in range(0, len(t)):
        print(t[i], end=" ")




#----------------- Serie 1 ex 04 --------------------*



def maximale(t):
    maxv = t[0]
    for i in range(0, len(t)):
        if t[i] > maxv:
            maxv = t[i]
    return maxv





#----------------- Serie 1 ex 05 --------------------*


def minimale(t):
    minv = t[0]
    for i in range(0, len(t)):
        if t[i] < minv:
            minv = t[i]
    return minv




#----------------- Serie 1 ex 06 --------------------*


def occurrence(t, x):
    occu = 0
    for i in range(0, len(t)):
        if t[i] == x:
            occu += 1
    return occu      




#----------------- Serie 1 ex 07 --------------------*


def premierP(t, x):
    index = None
    for i in range(0, len(t)):
        if t[i] == x:
            index = i+1
            return index
            


#----------------- Serie 1 ex 08 --------------------*

def derneirP(t, x):
    index = None
    for i in range(0, len(t)):
        if t[i] == x:
            index = i+1

    return index
    



#----------------- Serie 1 ex 09 --------------------*


def moyenne(t):
    somme = 0
    c = 0
    for i in range(0, len(t)):
        somme += float(t[i])
        c += 1
    return somme / c





#----------------- Serie 1 ex 10 --------------------*
Ncas = int(input("Donner le nombre de cas :"))
data = []

remplir(data, Ncas)
maxv = maximale(data)
print("La valeur maximale est :" , maxv)

print("le Nombre d'occurence de la valeur maximale :", occurrence(data, maxv))

print("Premeir occurence de la valeur maximale :", premierP(data, maxv))

print("Dernier occurence de la valeur maximale : ", derneirP(data, maxv))

minv = minimale(data)

print("La valeur Minimale est : ", minv)

print("le Nombre d'occurence de la valeur Minimale :", occurrence(data, minv))

print("Premeir occurence de la valeur Minimale : ", premierP(data, minv))

print("Dernier occurence de la valeur Minimale : ", derneirP(data, minv))

print("La valeur moyenne du tableu :", moyenne(data))

trier(data)

print("le tableau ordonné : ", data)







