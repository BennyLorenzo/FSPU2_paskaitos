# 3
query = 'SELECT * FROM DARBUOTOJAI WHERE SKYRIUS_PAVADINIMAS="Finansų";'
print(query)
query = 'INSERT INTO DARBUOTOJAI VALUES("Adomas", "Adomaitis", "1990-01-01", "Direktorius", "Naujas");'
print(query)
query = 'INSERT INTO DARBUOTOJAI (VARDAS, PAVARDĖ, SKYRIUS_PAVADINIMAS) VALUES("Nojus", "Naujokaitis", "Naujas");'
print(query)

skyrius = "Finansų"
query = f'SELECT * FROM DARBUOTOJAI WHERE SKYRIUS_PAVADINIMAS="{skyrius}";'
print(query)

vardas = "Adomas"
pavarde = "Adomaitis"
gimdata = "1990-01-01"
pareigos = "Direktorius"
skyrius = "Projektų"
query = f'INSERT INTO DARBUOTOJAI VALUES("{vardas}", "{pavarde}", "{gimdata}", "{pareigos}", "{skyrius}");'
print(query)