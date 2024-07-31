import sqlite3

# sukuriam susijungimą
conn = sqlite3.connect("asmenys.db")

# sukuriam kursorių
c = conn.cursor()

# užklausa
query = "SELECT * FROM asmenys;"

res = c.execute(query)
print(res)

fetch_res = res.fetchall()
print(fetch_res)

for item in fetch_res:
    print(item)

# ištriname nurodytus duomenis
query = 'DELETE FROM asmenys WHERE pavarde = "Adomėnas";'
c.execute(query)
conn.commit() # išsaugojimas DB faile

# patikriname, ar ištrynė
query = "SELECT * FROM asmenys;"
c.execute(query)
res = c.fetchall()
print(res)

# uždarome sujungimą
conn.close()
