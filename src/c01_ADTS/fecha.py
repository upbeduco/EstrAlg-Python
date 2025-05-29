# Exercise:
## Implement a Date ADT using the year,month,day representation

class Date:

    def __init__(self, year:int, month:int, day:int):
        self._year = year
        self._month = month
        self._day = day

    def day_of_the_year(self) -> int:
        # TODO Implementar el calculo del dia del año
        pass

    @staticmethod
    def is_leap_year(año: int) -> bool:
        # TODO Implementar la funcion para determinar si un año es biciesto
        pass

    def __str__(self) -> str:
        return f"{self._year:4d}-{self._month:02d}-{self._day:02d}"

    def __lt__(self, fecha) -> bool:
        # TODO Implementar la comparacion 'menor que' entre fechas
        pass

    def __eq__(self, fecha) -> bool:
        # TODO Implementar la igualdad entre instancias de Fecha
        pass

    @staticmethod
    def read_date() -> 'Date':
        """[Factory Pattern](https://refactoring.guru/design-patterns/factory-method)"""
        # TODO Leer una fecha por consola y returnar una instancia de Fecha
        pass


if __name__ == "__main__":

    cumple = Date.leerFecha()      # Invocar un método estático

    fecha = Date(2022,5,9)         # Invocar el constructor
    print(fecha)

    # TODO hacer pruebas unitarias de Fecha
    