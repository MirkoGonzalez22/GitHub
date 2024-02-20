import random

def imprimir_opciones():
    print("===============================")
    print("Piedra Papel Tijeras Lagarto Spock")
    print("===============================")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌️")
    print("4) 🦎")
    print("5) 🖖")

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == 1 and (computadora == 3 or computadora == 4)) or \
         (jugador == 2 and (computadora == 1 or computadora == 5)) or \
         (jugador == 3 and (computadora == 2 or computadora == 4)) or \
         (jugador == 4 and (computadora == 5 or computadora == 2)) or \
         (jugador == 5 and (computadora == 1 or computadora == 3)):
        return "¡Ganaste!"
    else:
        return "¡La computadora ganó!"

def piedra_papel_tijeras_lagarto_spock():
    imprimir_opciones()
    eleccion_jugador = int(input("Elige un número (1-5): "))
    if eleccion_jugador not in [1, 2, 3, 4, 5]:
        print("Selección inválida. Por favor elige un número entre 1 y 5.")
        return

    opciones = ["✊", "✋", "✌️", "🦎", "🖖"]
    simbolo_eleccion_jugador = opciones[eleccion_jugador - 1]
    
    eleccion_computadora = random.randint(1, 5)
    simbolo_eleccion_computadora = opciones[eleccion_computadora - 1]

    print("\nElegiste:", simbolo_eleccion_jugador)
    print("La CPU eligió:", simbolo_eleccion_computadora)

    print(determinar_ganador(eleccion_jugador, eleccion_computadora))

piedra_papel_tijeras_lagarto_spock()
