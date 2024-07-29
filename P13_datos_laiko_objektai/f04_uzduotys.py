import datetime

# 1, 2, 3, 4
current_date = datetime.datetime.today()

def calculate_time_from_birthday(user_input):
    try:
        user_birthday = datetime.datetime.strptime(user_input, "%Y %m %d")
    except:
        print("Netinkamas formatas, atskirkite duomenis tarpais.")
        return 0
    else:
        return current_date - user_birthday

# user_input = input("Įveskite savo gimimo metus, mėnesį, dieną, atskirtus tarpais: ")
user_input = "1996 01 19"
res = calculate_time_from_birthday(user_input)
if res != 0:
    print(f"Nuo jūsų gimtadienio praėjo {res.days} dienos arba ~{int(res.days / 30)} mėnesiai arba ~{round(res.days / 365, 1)} metai.")