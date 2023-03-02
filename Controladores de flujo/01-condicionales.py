"""Condicionales"""

EDAD = 22

# IF ELIF ELSE

if EDAD > 65:  # Si cumple con la condicion se ejecuta el codigo a continuecion
    print("Es mayor de 65 años")
elif EDAD > 18:  # Si no, si cumple con la condicion se ejecuta el codigo a continuecion
    print("Es mayor de 18 años")
else:  # Si no se cumple las condiciones se ejecutara el codigo a continuacion
    print("Es menor de 18 años")

# OPERADOR TERNARIO

MENSAJE = "Es mayor de 18 años" if EDAD > 18 else "Es menor de 18 años"

print(MENSAJE)

# OPERADORES LOGICOS
# and, or, not => "SI", "O", "NO"

LOGIN = False
PAGO = True

if LOGIN and PAGO:
    print("Puedes continuar")

if not LOGIN or not PAGO:
    print("No puedes continuar")

# CADERA DE COMPARACIONES

if 18 <= EDAD <= 65:
    print("Tiene entre 18 y 65 años")
