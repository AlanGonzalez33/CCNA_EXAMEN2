from math import *
import math

def calcular_circunferencia(radio):
    PI_perso = round(math.pi ,6)
    circu = radio * PI_perso * 2
    return circu

radios_soli = [3,8,10]

for radio in radios_soli:
    circunferencia = calcular_circunferencia(radio)

    print(f"la circunferencia de radio {radio}, es {circunferencia}")
