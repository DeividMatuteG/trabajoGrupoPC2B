tablero_xo = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

campo_tablero = []

for campo in tablero_xo:
    campo_tablero.append(campo)


def ver_tablero_xo(posicion):
    print(posicion['1'] + '|' + posicion['2'] + '|' + posicion['3'])
    print('-+-+-')
    print(posicion['4'] + '|' + posicion['5'] + '|' + posicion['6'])
    print('-+-+-')
    print(posicion['7'] + '|' + posicion['8'] + '|' + posicion['9'])

def tic_tac_toe():

    jugador = ' 1 '
    contador = 0


    for i in range(10):
        ver_tablero_xo(tablero_xo)
        print("Turno de " + jugador + "Escoge la posicón que deseas")

        movimiento = input()        

        if tablero_xo[movimiento] == ' ':
            tablero_xo[movimiento] = jugador
            contador += 1
        else:
            print("Este campo ya se encuentra ocupado")
            continue

        if contador >= 5:
            if tablero_xo['1'] == tablero_xo['2'] == tablero_xo['3'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!")                
                
            elif tablero_xo['4'] == tablero_xo['5'] == tablero_xo['6'] != ' ':
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!")  
                
            elif tablero_xo['7'] == tablero_xo['8'] == tablero_xo['9'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!")  
               
            elif tablero_xo['1'] == tablero_xo['4'] == tablero_xo['7'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!") 
                
            elif tablero_xo['3'] == tablero_xo['5'] == tablero_xo['8'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!") 
                
            elif tablero_xo['3'] == tablero_xo['6'] == tablero_xo['9'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!") 
               
            elif tablero_xo['1'] == tablero_xo['5'] == tablero_xo['9'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("La fila se ha completado")                
                print("El ganador es: " +jugador + " ¡Felicidades!") 
                
            elif tablero_xo['3'] == tablero_xo['5'] == tablero_xo['7'] != ' ': 
                ver_tablero_xo(tablero_xo)
                print("Parece que el juego a terminado")                
                print("El ganador es: " +jugador + " ¡Felicidades!") 
                break 

        
        if contador == 9:
           print("Parece que el juego a terminado")                
           

        
        if jugador ==' 1 ':
            jugador = ' 0 '
        else:
            jugador = ' 1 '        
        

if __name__ == "__main__":
    tic_tac_toe()

    