import f05_atributu_modifikatoriai as fmod

print(fmod.daugink(5, 6))

print(fmod.paprastas_skaicius)

print(fmod._skaicius) # perspėjimas apie apsaugą

print(fmod.__privatus_skaicius)

print(fmod._sudek(1, 5)) # perspėjimas apie apsaugą

print(fmod.__atimk(10, 5))

from f05_atributu_modifikatoriai import _sudek, __atimk

print(_sudek(1, 7))
print(__atimk(7, 1))

# kintamuosius ir metodus techniškai eina naudoti, bet nereikėtų

import random
import datetime

# from random import - autocomplete nerodo apsaugotų, privačių pasirinkimų



