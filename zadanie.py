import random

podaj_najniższą=int(input("Podaj podłogę: "))
podaj_najwyższą=int(input("Podaj sufit: "))


c=random.randint(podaj_najniższą,podaj_najwyższą)

def sprawdzanie(c):

    if zgadnij_liczbę==c:
        print(f"Zgadza się, liczba to {c}")
        return True
    elif zgadnij_liczbę>c:
        print("liczba za duża")
    elif zgadnij_liczbę<c:
        print("liczba za mała")


while True:
    zgadnij_liczbę = int(input("Zgadnij liczbę"))
    if sprawdzanie(c):
        break
