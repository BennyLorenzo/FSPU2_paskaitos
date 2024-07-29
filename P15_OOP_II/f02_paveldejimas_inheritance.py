"""Paveldėjimas objektiniame programavime suteikia galimybę sudaryti
tėvines klases su bendromis savybėmis, bei metodais ir vaikines kurios
gali naudoti ir tėvinės ir savo metodus, bei keisti tėvinėj klasėj aprašytą
metodą savuoju."""


class Gyvunas:
    """Tėvinė klasė visoms gyvūnų rūšims,
    Kate, Shuo, Papuga paveldės ir galės
    naudoti viską kas čia aprašyta"""

    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def __str__(self):
        return f"{self.vardas} {self.spalva}"

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

    def juoktis(self):
        print(f"{self.vardas} HA HA!")


class Kate(Gyvunas):  # paveldėjimo sintaksė (Gyvunas)
    """Kate turi viską iš Gyvunas klasės,
    bei papildomai turi savo
    individualų metodą miaukseti"""
    def miaukseti(self):
        print(f"{self.vardas} sako miau miau")


class Shuo(Gyvunas): # paveldėjimo sintaksė (Gyvunas)
    """Shuo turi viską iš Gyvunas klasės,
    bei papildomai turi savo
    individualų metodą loti"""
    def loti(self):
        print(f"{self.vardas} sako au au")


class Papuga(Gyvunas): # paveldėjimo sintaksė (Gyvunas)
    """Papuga neturi papildomo metodo,
    bet ji turėdama viską iš Gyvunas klasės,
    pakeičia Gyvuno klasės metodo juoktis
    darbą, jį perrašydama(override)"""
    def juoktis(self):
        print(f"{self.vardas} aš PAPŪGA aš nesijuokiu, o KVATOJU kaip BOSAS"
              f"HA HA HA HA HA HA HA HA HA HA HA HA HA HA HA")


kate1_o = Kate("Rainė", "raina")
kate1_o.begti()
kate1_o.miaukseti()
kate1_o.juoktis()
print(kate1_o)
print("--------")

kate2_o = Kate("Alisa", "balta")
kate2_o.begti()
kate2_o.miaukseti()
kate2_o.juoktis()
print(kate2_o)
print("--------")

shuo1_o = Shuo("Reksas", "margas")
shuo1_o.begti()
shuo1_o.loti()
shuo1_o.juoktis()
print(shuo1_o)
print("---------")

papuga1_o = Papuga("Čarlis", "ryškiai geltona")
papuga1_o.begti()
papuga1_o.juoktis()
print(papuga1_o)
