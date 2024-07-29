# 1c
from f02_uzduotys import Knyga

biblioteka = []
# i = 0
while True:
    user_input = input("Įveskite knygos pavadinimą, autorių ir puslapių skaičių, atskirtus kableliu: ")
    user_data = user_input.split(",")
    biblioteka.append(Knyga(user_data[0], user_data[1], int(user_data[2]), 0))
    prideti_dar = input("Ar norite pridėti dar vieną knygą? (taip/ne): ")
    if prideti_dar == "ne":
        print("Įvestų knygų sąrašas: ")
        for knyga in biblioteka:
            print(knyga)
        print("Programa baigė darbą.")
        break