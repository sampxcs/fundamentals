"""CALCULADORA 02"""

print("""
Bienvenido a la carculadora en la terminal.
Ingrese los numeros y el tipo de operacion que quiere realizar.

Las operaciones son:
        Suma => "+"
        Resta => "-"
        Multiplicacion => "*"
        Division => "/"

Cuando quieras salir ingresa el comando "salir"
""")

COMAND = ""

while True:

    COMAND = input("Ingrese el primer numero: ")
    if COMAND != "salir":
        N1 = int(COMAND)
    else:
        break

    COMAND = input("Ingrese el tipo de operacion: ")
    if COMAND != "salir":
        op = COMAND.lower()
    else:
        break

    COMAND = input("Increse el segundo numero: ")
    if COMAND != "salir":
        N2 = int(COMAND)
    else:
        break

    if op == "+":
        print("Resultado: ", N1 + N2)

    if op == "-":
        print("Resultado: ", N1 - N2)

    if op == "*":
        print("Resultado: ", N1 * N2)

    if op == "/":
        print("Resultado: ", N1 / N2)
