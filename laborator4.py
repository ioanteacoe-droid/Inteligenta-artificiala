#Exercitiul 1

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]
for row in picture:
    for numar in row:
        if numar == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

    #Exercitiul 2
# nota = float(input("Introdu nota examenului (1-10): "))
#
# if nota < 1 or nota > 10:
#     print("Notă invalidă!")
# elif nota >= 9:
#     print("Excelent")
# elif nota >= 7:
#     print("Bine")
# elif nota >= 5:
#     print("Suficient")
# else:
#     print("Reexaminare")

    # Exercitiul 3
    # import random
    #
    # numar_secret = random.randint(1, 50)
    # incercari = 0
    #
    # print("Am ales un număr între 1 și 50. Ghicește-l!")
    #
    # guess = 0
    #
    # while guess != numar_secret:
    #     guess = int(input("Ghiceste numarul (1-50): "))
    #     incercari += 1
    #     if guess < numar_secret:
    #         print("Numarul este mai mare!")
    #     elif guess > numar_secret:
    #         print("Numarul este mai mic!")
    #
    # print("Perfect! Ai ghicit numarul in", incercari, "incercari.")

    # Exercitiul 4
    # orase = ["București", "Cluj-Napoca", "Timișoara", "Iași"]
    #
    # for index, oras in enumerate(orase, start=1):
    #     print(f"{index}. {oras}")

        # Exercitiul 5

    # import random
    #
    # print("Bine ai venit la Loteria Python!")
    # print("Alege 6 numere între 1 și 49.")
    #
    # # 1. Citim numerele de la utilizator
    # numere_alese = []
    # for i in range(1, 7):
    #     n = int(input(f"Numărul {i}: "))
    #     numere_alese.append(n)
    #
    # # 2. Generăm 6 numere extrase (fără să se repete)
    # numere_extrase = random.sample(range(1, 50), 6)
    #
    # # 3. Găsim numerele comune (ghicite)
    # ghicite = [n for n in numere_alese if n in numere_extrase]
    #
    # # 4. Afișăm rezultatele
    # print(f"\nNumere extrase: {numere_extrase}")
    # print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")
    #
    # # 5. Mesaj de câștig în funcție de rezultat
    # if len(ghicite) == 6:
    #     print("WOW! Ai câștigat MARELE PREMIU!")
    # elif len(ghicite) >= 3:
    #     print("Felicitări! Ai câștigat un premiu mic!")
    # else:
    #     print("Mai încearcă, data viitoare va fi cu noroc!")
    #
        # Exercitiul 6


