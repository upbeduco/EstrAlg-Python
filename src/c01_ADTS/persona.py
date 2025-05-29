# ADT Persona
# An ADT representing personal data of an individual

from dataclasses import dataclass
from fecha import Date


@dataclass(order=True)
class Persona:
    edad: int
    nombre: str
    fechaNacimiento: Date


if __name__ == "__main__":
    p1 = Persona(32, "Juan", Date(1990,4,20))
    p2 = Persona(27, "Maria", Date(1995,9,11))
    p3 = Persona(34, "Laura", Date(1988,7,2))

    print(p1)
    print(p2)    
    print(p3)    
    assert p1>p2, "p1 es mayor a p2"
    assert p2<p3, "p2 es menor a p3"
    assert not(p3<p1), "p3 no es menor a p1"