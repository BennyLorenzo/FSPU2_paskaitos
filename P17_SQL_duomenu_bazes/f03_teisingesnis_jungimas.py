import sqlite3

conn = sqlite3.connect("asmenys2.db")  # sukuriam susijungimą
c = conn.cursor()  # sukuriam kursorių

query = """
CREATE TABLE IF NOT EXISTS asmenys(
vardas TEXT,
pavarde TEXT,
gimetai INTEGER,
atlyginimas REAL
);"""
with conn:
    c.execute(query)



def select_all_print():
    print("-------------------------------------------")
    with conn:
        c.execute("SELECT ROWID, * FROM asmenys;")
        db_results = c.fetchall()
    for res in db_results:
        print(res)
    print("-------------------------------------------")

select_all_print()

# query = "SELECT * FROM asmenys;"  # užklausa
# with conn:  # konteksto sakinys, kontekstas - susijungimas su DB
#     c.execute(query)
#     fetch_res = c.fetchall()
#
# print(fetch_res)  # duomenys pateikiami iš DB ir atspausdinami

# with conn:
#     c.execute('INSERT INTO asmenys VALUES ("Adomas","Adamauskas",2000,999)')
#     c.execute('INSERT INTO asmenys VALUES ("Raimundas","Radamauskas",2005,999)')
#     c.execute('INSERT INTO asmenys VALUES ("Naujalis","Naujokaitis",2001,999)')

# with conn:
#     c.execute('DELETE FROM asmenys WHERE atlyginimas = 999')

# įterpimas pagal vartotojo įvestus vardą ir pavardę
print("ĮTERPIMAS")
user_input = input("Įveskite vardą, pavardę, gimimo metus ir atlyginimą, atskirtus kableliais: ")
if user_input == "q":
    pass
else:
    user_data = user_input.split(",")
    name = user_data[0]
    surname = user_data[1]
    birth_year = int(user_data[2])
    salary = float(user_data[3])
    insert_query = f'INSERT INTO asmenys VALUES ("{name}","{surname}",{birth_year},{salary})'
    with conn:
        c.execute(insert_query)

select_all_print()

# trynimas pagal vartotojo įvestus vardą ir pavardę
print("TRYNIMAS PAGAL VARDĄ, PAVARDĘ")
user_input = input("Įveskite vardą ir pavardę, atskirtus kableliais: ")
if user_input == "q":
    pass
else:
    user_data = user_input.split(",")
    name = user_data[0]
    surname = user_data[1]

    delete_query = f'DELETE FROM asmenys WHERE vardas = "{name}" AND pavarde = "{surname}"'
    with conn:
        c.execute(delete_query)

select_all_print()
# trynimas pagal vartotojo row id
print("TRYNIMAS PAGAL ROW ID")
row_id = input("Įveskite ROW ID: ")
if row_id == "q":
    pass
else:
    delete_query = f'DELETE FROM asmenys WHERE ROWID = {int(row_id)}'
    with conn:
        c.execute(delete_query)

select_all_print()

# atlyginimo atnaujinimas pagal vartotojo įvestus vardą, pavardę
print("ATLYGINIMO ATNAUJINIMAS")
user_input = input("Įveskite vardą,pavardę ir naują atlyginimą atskirtus kableliais: ")
if user_input == "q":
    pass
else:
    user_data = user_input.split(",")
    name = user_data[0]
    surname = user_data[1]
    new_salary = user_data[2]
    update_query = f'UPDATE asmenys SET atlyginimas={float(new_salary)} WHERE' \
                   f' vardas = "{name}" AND pavarde = "{surname}"'
    with conn:
        c.execute(update_query)

select_all_print()