#Problema cu triunghiul lui pascal alta varianta cu Combinari
import math

def factorial(n):
   " Calculeaz factorialul unui număr întreg n"
   return math.factorial(n)

def combinari(n, k):
    " Calculează combinările de n luate câte k (C_n^k). "
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    # Aplica formula C_n^k = n! / (k! * (n-k)!)
    return factorial(n) // (factorial(k) * factorial(n - k))

def triunghi_pascal_combinari(numar_randuri):
    " Generează Triunghiul lui Pascal folosind formula combinărilor. "
    triunghi = []
    for n in range(numar_randuri):
        rand_curent = []
        # Pe rândul 'n' avem n+1 elemente, de la k=0 la k=n
        for k in range(n + 1):
            valoare = combinari(n, k)
            rand_curent.append(valoare)
        triunghi.append(rand_curent)
    return triunghi

# Exemplu de utilizare
N = 6
rezultat = triunghi_pascal_combinari(N)

# Afișarea triunghiului
print(f"Triunghiul lui Pascal (folosind C(n, k)) pentru {N} rânduri:")
for rand in rezultat:
    print(rand)
