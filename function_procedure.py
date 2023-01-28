#----------------- Serie 1 ex 01 --------------------*
'''

def remplir(t):
    for i in range(0, len(t)):
        t.append(input("Denner un valeur"))
    

'''

#----------------- Serie 1 ex 02 --------------------*
'''

def trier(t):
    for i in range(0, len(t)):
        for j in range(0, len(t)-i-1):
            if t[j] > t[j + 1]:
                    t[j] , t[j+1] = t[j+1], t[j]

'''


#----------------- Serie 1 ex 03 --------------------*
'''

def afficher(t):
    for i in range(0, len(t)):
        print(t[i], end=" ")


'''

#----------------- Serie 1 ex 04 --------------------*

'''

def maximale(t):
    maxv = t[0]
    for i in range(0, len(t)):
        if t[i] > maxv:
            maxv = t[i]
    return maxv

'''



#----------------- Serie 1 ex 05 --------------------*
'''

def minimale(t):
    minv = t[0]
    for i in range(0, len(t)):
        if t[i] < minv:
            minv = t[i]
    return minv


'''

#----------------- Serie 1 ex 06 --------------------*
'''

def occurrence(t, x):
    occu = 0
    for i in range(0, len(t)):
        if t[i] == x:
            occu += 1
    return occu      



'''
#----------------- Serie 1 ex 07 --------------------*

