# 1c
import pickle
from P14_uzduotys import Knyga

try:
    with open('biblioteka.pickle', mode='rb') as failas:
        biblioteka = pickle.load(failas)
except:
    print("Failas nerastas!")
    biblioteka = []

while True:
    print("--------------------\n"
          "1. Įvesti knygą\n"
          "2. Rodyti visas knygas\n"
          "3. Išeiti iš programos\n")
    user_choice = input("Įveskite pasirinkimą: ")
    if user_choice == "1":
        user_input = input("Įveskite knygos pavadinimą, autorių ir puslapių skaičių, atskirtus kableliu: ")
        user_data = user_input.split(",")
        biblioteka.append(Knyga(user_data[0], user_data[1], int(user_data[2]), 0))
        with open('biblioteka.pickle', mode='wb') as failas:
            pickle.dump(biblioteka, failas)
    elif user_choice == "2":
        if len(biblioteka) == 0:
            print("Knygų sąrašas tuščias.")
        else:
            print("Knygų sąrašas:")
            for knyga in biblioteka:
                print(knyga)
    elif user_choice == "3":
        print("Programa baigė darbą.")
        break
    else:
        print("Tokio pasirinkimo nėra!")