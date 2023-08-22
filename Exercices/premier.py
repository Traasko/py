def est_premier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

nombre = int(input("Entrez un nombre : "))

print(f"Les nombres premiers entre 0 et {nombre} sont :")
for i in range(2, nombre + 1):
    if est_premier(i):
        print(i, end=" ")
print()  
