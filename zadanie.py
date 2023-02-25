import random

min=int(input("Podaj podłogę: "))
max=int(input("Podaj sufit: "))


c=random.randint(min, max)

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
