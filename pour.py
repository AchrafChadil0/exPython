


#----------------- Serie 2 ex 01 --------------------

"""

n , m = int(input("Donner premier entier :")), int(input("donner deuxieme entier :"))
min = 0
div = 0
if ( n < m):
    min = n
else:
    min = m

for i in range(1, min):
    if (n % i == 0 and m % i == 0):
        div = i

print("Le plus grand divisuer commun", div)


"""


#----------------- Serie 2 ex 02 --------------------

'''


n , m = int(input("Donner premier entier :")), int(input("donner deuxieme entier :"))

mult = 0

for i in range(m*n, 1, -1):
    if (i % n == 0 and i % m == 0):
        mult = i

print("Le plus petit multiplicateur", mult)


'''

#----------------- Serie 2 ex 03 --------------------

'''

n = int(input("Donner un entier :"))
t = 0
for i in range(2, n-1):
    if n % i == 0:
        t = 1

print("le nomber n'est pas premier.") if t == 1 else print("le nomber est premier.")

'''



#----------------- Serie 2 ex 04 --------------------
'''


n = int(input("Donner un entier :"))
s = 0
for i in range(1, n-1):
    if (n % i == 0):
        s = s+i
if (n % s == 0):
    print(n," est devirsable par la somme de ses deviseurs entre 1 à ", n-1)
else:
    print(n, "n'est pas diversable par la somme de ses deviseurs entre 1 à ", n -1)



'''

#----------------- Serie 2 ex 06 --------------------


'''
n = int(input("Donner un entier : "))
lenght = len(str(n))
s = 0

for x in range(0, lenght):
    r = n % 10
    s = s*10 + r
    n = n // 10
    

print("le resumtat est: ", s)


'''

#----------------- Serie 2 ex 07 --------------------

'''

s = 0

for i in range(0, 5):
    n = int(input("Donner un entier : "))
    s = s + n

moy = s / 5
print("La valeur moyenne", moy)

'''

#----------------- Serie 2 ex 08 --------------------

n = int(input("Donner un entier : "))
maxv = n
minv = n

