import pickle
from f07_laukai import Namas

with open('namai.pickle', mode='rb') as failas:
    kaupiklis = pickle.load(failas)
print("---------------")
while True:
    ivestis = input("Įveskite metus, arba q - pabaigti įvestį: ")
    if ivestis == "q":
        break
    metai = int(ivestis)
    kaina = float(input("Įveskite kainą: "))

    naujas_namo_obj = Namas(kaina, metai)
    kaupiklis.append(naujas_namo_obj)

    for namo_obj in kaupiklis:
        print(namo_obj)

with open('namai.pickle', mode='wb') as failas: # wb - write binary
    pickle.dump(kaupiklis, failas)


