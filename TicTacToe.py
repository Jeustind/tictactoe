tablero = [' ' for _ in range (9)]

def print_tablero():
    fila = ''
    for i in range (9):
        if (i + 1) % 3 == 0:
            fila += f'{tablero[i]}'
            print(fila)
            if i != 8:
                print('_'* 9)
            fila = ''  
        else:
            fila += f' {tablero[i]} |'
                
def verificar_victoria(jugador):
                    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
                    for c in combinaciones:
                        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] == jugador:
                            return True
                    return False

def verificar_empate():
            return ' ' not in tablero
            
def jugar(): 
            jugador = 'X'
            while True:
                print_tablero()
                print(f'Es el turno del jugador {jugador}')
                posición = int(input('Ingrese una posición:')) -1
                if tablero[posición] == ' ':
                 tablero[posición] = jugador
                 if verificar_victoria(jugador):
                        print_tablero()
                        print(f'Judador {jugador} ha ganado')
                        break 
                if verificar_empate():
                        print_tablero()
                        print ('Empate')
                        break
                jugador = 'O' if jugador == 'X' else 'X'
            else:
                print('Posición ocupada')
jugar()