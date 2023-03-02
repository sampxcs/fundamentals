"""TERMINAL APP"""

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
