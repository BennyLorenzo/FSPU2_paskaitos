# 1a. Programa priima vartotojo įvestus
# gimimo metus, paskaičiuoja jo amžių
# ir atspausdina.
# 1b. Tas pats tik atspausdina su tekstu "Jums yra x metų"

from datetime import datetime
current_year = datetime.today().year

user_birth_year = int(input("Įveskite savo gimimo metus: "))
user_age = current_year - user_birth_year
print("Jums yra " + str(user_age) + " metų")

# 2a. Programa priima vartotojo įvestą amžių,
# paskaičiuoja gimimo metus ir atspausdina.
# 2b. Tas pats tik su tekstu "Jūs gimėt x metais"

user_age = int(input("Įveskite savo amžių: "))
user_birth_year = current_year - user_age
print("Jūs gimėte " + str(user_birth_year) + " metais")

# 3. Programa priima vartotojo vardą ir gimimo metus,
# atspausdina vardą ir amžių.

user_name = input("Iveskite savo vardą: ")
user_birth_year = int(input("Įveskite savo gimimo metus: "))
user_age = current_year - user_birth_year
print("Sveiki, " + user_name + ", Jums yra " + str(user_age) + " metų")

# 4. Programa priima vartotojo vardą ir
# atspausdina jį atbulai vienoje eilutėje,
# kitoje eilutėje didžiosiomis

user_name = (input("Įveskite savo vardą: "))
print(user_name[::-1])
print(user_name.upper())

# 5. pasinaudojus dokumentacija susirasti keletą str metodų,
# nenaudotų paskaitoje ir panaudoti savo kode

print(user_name.partition("ry"))
print(user_name.zfill(20))