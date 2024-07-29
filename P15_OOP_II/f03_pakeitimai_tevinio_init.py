

class Asmuo:
    def __init__(self, vardas, pavarde, amzius):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.amzius} __str"

    def __repr__(self):
        return f"{self.vardas} {self.pavarde} {self.amzius} __repr"

asmuo = Asmuo("Jonas","Jonaitis",25)
print(asmuo)


class MokinioTevas(Asmuo):
    def __init__(self, vardas, pavarde, amzius, darboviete):
        super().__init__(vardas, pavarde, amzius)
        self.darboviete = darboviete

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.amzius} {self.darboviete}"

asmuo2 = MokinioTevas("Antanas","Antanaitis",35,"VU")
print(asmuo2)

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, amzius, mokykla, grupe):
        super().__init__(vardas, pavarde, amzius)
        self.mokykla = mokykla
        self.grupe = grupe
        self.tevai = []

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.amzius} {self.mokykla} {self.grupe} {self.tevai}"

    def priskirti_tevus(self, tevas):
        self.tevai.append(tevas)

asmuo3 = Mokinys("Julius","Julėnas",14,"Licėjus","D")
print(asmuo3)

asmuo3.priskirti_tevus(asmuo2)
print(asmuo3)
