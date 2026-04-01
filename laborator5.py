import functools
lis = [1, 3, 5, 6, 2]

print(" The sum of the list elements is: ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

print(" The maximum element of the list is: ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# Ex 1
# Joc Piatră-Hârtie-Foarfecă

# vrea_sa_joace = "da"
#
# while vrea_sa_joace == "da":
#     # 1. Citim alegerile
#     j1 = input("Jucător 1: ").lower()
#     j2 = input("Jucător 2: ").lower()
#
#     # 2. Verificăm cine a câștigat
#     if j1 == j2:
#         print("Egalitate!")
#     elif (j1 == "piatra" and j2 == "foarfeca") or \
#          (j1 == "foarfeca" and j2 == "hartia") or \
#          (j1 == "hartia" and j2 == "piatra"):
#         print("Felicitări Jucător 1! Ai câștigat.")
#     else:
#         print("Felicitări Jucător 2! Ai câștigat.")
#
#     # 3. Întrebăm de reluare
#     vrea_sa_joace = input("Mai jucați? (da/nu): ").lower()
#
# print("Joc încheiat!")

# Ex 2
def genereaza_factura(nume_client, **produse):
    print(f"Factură pentru: {nume_client}")
    print("-" * 30)

    total = 0
    # Parcurgem dicționarul de produse (nume și preț)
    for produs, pret in produse.items():
        print(f"{produs}: {pret} RON")
        total += pret

    print("-" * 30)
    print(f"Total de plată: {total} RON")


# Exemplu de utilizare:
genereaza_factura("Ionescu Andrei", Paine=3, Lapte=7, Ciocolata=12)

# Ex 3
import random


def normalize_data(lista):
    # Verificăm dacă lista nu este goală pentru a evita erori
    if not lista:
        return []

    minim = min(lista)
    maxim = max(lista)

    # Verificăm dacă toate numerele sunt identice (pentru a evita împărțirea la 0)
    if maxim == minim:
        return [0.0] * len(lista)

    # Calculăm lista normalizată
    rezultat = []
    for x in lista:
        valoare_noua = (x - minim) / (maxim - minim)
        rezultat.append(valoare_noua)

    return rezultat


# 1. Testare cu exemplul dat
data = [10, 20, 30, 40, 50]
print(f"Date originale: {data}")
print(f"Normalizate: {normalize_data(data)}")

# 2. Testare cu un set de date aleator
# Generăm 5 numere la întâmplare între 1 și 100
date_aleatorii = [random.randint(1, 100) for _ in range(5)]
print(f"\nDate aleatorii: {date_aleatorii}")
print(f"Normalizate: {normalize_data(date_aleatorii)}")
