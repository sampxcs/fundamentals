"""TO DO LIST"""


def app():
    """app"""

    print("""
    Bienvenido a to-do-list

    Ingresa tus tareas con el comando "INSERT"
    Ve lo que tienes en tu lista con el comando "SHOW"

    Para salir usa el comando "EXIT"
    """)

    lista = []

    while True:
        comand = input(">>>").upper()

        if comand.startswith("INSERT"):
            element = comand.replace("INSERT", "").strip().capitalize()
            lista.append(element)
            print("Dato insertado correctamente")

        if comand.startswith("SHOW"):
            for index, element in enumerate(lista):
                print(index + 1, element)

        if comand.startswith("EXIT"):
            print("Hasta pronto")
            break


app()
