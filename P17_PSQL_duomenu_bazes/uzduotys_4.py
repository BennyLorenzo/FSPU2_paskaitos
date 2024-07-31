# 4
import sqlite3

conn = sqlite3.connect("cars_uzduotis.db")  # sukuriam susijungimą
c = conn.cursor()  # sukuriam kursorių


def select_all_print():
    with conn:
        c.execute("SELECT ROWID, * FROM cars;")
        db_results = c.fetchall()
    for res in db_results:
        print(res)


def select_make_model_print(make, model):
    with conn:
        c.execute(f'SELECT ROWID, * FROM cars WHERE make = "{make}" AND model = "{model}";')
        db_results = c.fetchall()
    for res in db_results:
        print(res)


while True:
    print("---------------------------------------------------------------------\n"
          "1. Atspausdinti visus automobilius\n"
          "2. Įvesti naują automobilį\n"
          "3. Ištrinti automobilius pagal make ir model(vartotojo įvestus)\n"
          "4. Pakeisti kainą pagal rowid\n"
          "5. Surasti ir atspausdinti tik tam tikro make ir model automobilius\n"
          "q. Išeiti iš programos\n"
          "---------------------------------------------------------------------")
    menu_choice = input("Pasirinkite funkciją: ")
    if menu_choice == "1":
        select_all_print()
    elif menu_choice == "2":
        # 'Mazda', 'Mazda6', 'Fuscia', 2013, 85112)
        car_input = input("Įveskite naujo automobilio gamintoją, modelį, spalvą, metus ir kainą, atskirtus kableliu: ")
        car_data = car_input.split(",")
        car_make = car_data[0]
        car_model = car_data[1]
        car_color = car_data[2]
        car_year = int(car_data[3])
        car_price = float(car_data[4])
        insert_query = f'INSERT INTO cars VALUES ("{car_make}","{car_model}","{car_color}",{car_year},{car_price})'
        with conn:
            c.execute(insert_query)
    elif menu_choice == "3":
        car_input = input("Įveskite automobilio gamintoją ir modelį, atskirtus kableliu: ")
        car_data = car_input.split(",")
        car_make = car_data[0]
        car_model = car_data[1]
        delete_query = f'DELETE FROM cars WHERE make = "{car_make}" AND model = "{car_model}"'
        with conn:
            c.execute(delete_query)

    elif menu_choice == "4":
        car_input = input("Įveskite automobilio rowid ir naują kainą, atskirtus kableliu: ")
        car_data = car_input.split(",")
        car_row_id = car_data[0]
        new_price = car_data[1]
        update_query = f'UPDATE cars SET price={float(new_price)} WHERE' \
                       f' ROWID = {car_row_id}'
        with conn:
            c.execute(update_query)

    elif menu_choice == "5":
        car_input = input("Įveskite automobilio gamintoją ir modelį, atskirtus kableliu: ")
        car_data = car_input.split(",")
        car_make = car_data[0]
        car_model = car_data[1]
        select_make_model_print(car_make, car_model)

    elif menu_choice == "q":
        print("Programa baigė darbą.")
        break
    else:
        print("Toks pasirinkimas nerastas!")