import time


# 1
def skaiciuok():
    skaitliukas = 0
    while skaitliukas >= 0:
        yield skaitliukas
        skaitliukas += 1


for i in skaiciuok():
    time.sleep(0.5)
    print(i)


# 2
def skaiciuok_nuo(sk):
    skaitliukas = sk
    while True:
        yield skaitliukas
        skaitliukas += 1


for i in skaiciuok_nuo(200):
    time.sleep(0.5)
    print(i)


# 3
def skaiciuok_fibonaci():
    skaitliukas = 0
    pirmas = 0
    antras = 0
    while True:
        if skaitliukas == 0:
            antras = 1
            yield skaitliukas
            skaitliukas += 1
        yield skaitliukas
        pirmas = antras
        antras = skaitliukas
        skaitliukas = pirmas + antras


for i in skaiciuok_fibonaci():
    time.sleep(0.5)
    print(i)
