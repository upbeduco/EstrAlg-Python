# ADT Fecha
# Implementation using Python's Data classes

from dataclasses import dataclass

@dataclass(order=True)
class Fecha:
    año: int
    mes: int
    dia: int


if __name__=='__main__':
    f1 = Fecha(2022,5,20)
    f2 = Fecha(1999,1,1)
    f3 = Fecha(1642,12,25)
    print(f1,f2,f3)

# Ejercicios
# 1. Tiene Fecha metodo __str__ ?
# 2. Se pueden comparar fechas?
# 3. Como determinar si una fecha cae en año es biciesto?
# 4. Como calcular tiempo transcurrido entre 2 fechas?
# 5. Se pueden hacer validaciones para garantizar la integridad de los datos Fecha?

