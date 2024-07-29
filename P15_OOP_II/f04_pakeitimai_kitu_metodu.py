

class Mygtukas: # tarkime, jog ši klasė nepreinama redagavimui

    def __init__(self, x, y, plotis, uzrasas, spalva='pilkas'):
        self.x = x
        self.y = y
        self.plotis = plotis
        self.uzrasas = uzrasas
        self.spalva = spalva

    def __str__(self):
        return f"{self.spalva.capitalize()} mygtukas {self.uzrasas}."

    def deaktyvuoti(self):
        print(f"Mygtukas {self.uzrasas} deaktyvuotas.")


class RaudonasMygtukas(Mygtukas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spalva = "raudonas"

    def deaktyvuoti(self):
        super().deaktyvuoti()
        self.spalva = "pilkas"

mygt1 = RaudonasMygtukas(10, 10, 20, "OK")
mygt2 = RaudonasMygtukas(20, 20, 20, "Cancel")
mygt3 = RaudonasMygtukas(30, 30, 20, "Open")
mygt4 = RaudonasMygtukas(40, 40, 20, "Save")

print(mygt1)
print(mygt2)
print(mygt3)
print(mygt4)

mygt1.deaktyvuoti()
mygt1.spalva = "pilkas"

mygt2.deaktyvuoti()
mygt2.spalva = "pilkas"

print(mygt1)
print(mygt2)