"""TERMINAL APP"""

# Crea un bucle que este escuchando siempre
# la consola e imprima todos los comandos que le pasemos
# el bucle finaliza cuando se escribe el comando "salir"


# ------------------------------------------------ #
#                EJERCICIO RESUELTO                #
# ------------------------------------------------ #

print(
    """
    Aplicacion iniciada.
    Escriba los comando que quiere que aparezcan en consola.

    Si desea salir de la app pruebe el comando "salir".
    """
)

COMANDO = ""

while COMANDO.lower() != "salir":
    COMANDO = input("=> ")
    print(COMANDO)
