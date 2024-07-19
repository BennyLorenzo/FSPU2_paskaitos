skaitiklis = 0
while skaitiklis < 5:
    print("Skaitiklis yra: ",skaitiklis)
    print("---------")
    skaitiklis += 1

while True:
    ivestis = input("Įveskite žodį arba break: ")
    if ivestis == "break":
        print("Programa baigė darbą.")
    else:
        print("Įvedėte: ", ivestis)