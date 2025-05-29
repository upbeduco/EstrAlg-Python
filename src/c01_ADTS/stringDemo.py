# Comparing values vs. comparing references

s = "Hola Mundo"
t = input("Ingrese una frase: ")

print('Tipos de datos:', type(s), type(t))

# En Python el operador '==' está sobrecargado por el metodo __eq__ de la clase String
print(f's == t : {s==t}')

# El operador 'is' compara las referencias a los objetos
print(f's is t  : {s is t}')