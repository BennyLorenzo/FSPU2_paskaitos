autos_ger = ['BMW', 'Audi', 'Porsche']
autos_it = ['Ferrari', 'Lamborghini', 'Fiat']
autos_fr = ['Renault']
autos_jp = ['Mazda', 'Honda']
autos_us = ['Chevrolet', 'Dodge']
autos_sport = ['Ferrari', 'Lamborghini', 'BMW', 'Porsche']

auto = 'Audi'
all_autos = autos_us + autos_it + autos_jp + autos_ger + autos_sport + autos_fr

'''
if auto in autos_ger or auto in autos_fr or auto in autos_it:
    print(auto, "automobilis europietiškas")
else:
    print(auto,"automobilis ne europietiškas")

if auto in autos_it and auto in autos_sport:
    print(auto,"yra sportinis itališkas automobilis")
else:
    print(auto,"yra triperis")

if not (auto in autos_jp):
    print(auto,"nėra japoniškas")
else:
    print(auto,"yra japoniškas")'''

for auto in all_autos:
    # vykdymo eiga: in, and, or, todėl neteisingai Audi priskiria true, jei neapskliaudžiam or
    if (auto in autos_ger or auto in autos_it) and auto in autos_sport:
        print(auto, "sportinis, vokiškas arba itališkas")
    else:
        print(auto, "nėra sportinis itališkų-vokiškų")

