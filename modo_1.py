# azul 9 inicio de ruta
# verde 1 caminar un espacio direcci'on idxicada
# rojo 2 detener 5s antes de continuar con la ruta
# gris 3 pared, activar disparo
# morado 4 seguir hasta el extremo ignorando el resto de intrucciones
# naranja 5 retroceso de ruta

from ast import Return


def start(list):
    j=0
    for i in list: 
        if i//10 == 9:
            break
        else:
            j+=1
    return j

def color2(list):#funcion de prueba
    j=0
    for i in list: 
        if i !=0:
            if i//10 == 1:
                print(j,'= verde, avanza un espacio')
                return 1
            elif i//10 ==2:
                print(j,'= rojo, se detiene 5s y continua ruta')
                return 2
            elif i//10 == 3:
                print(j,'= gris, dispara')
                return 3
            elif i//10 == 4:
                print(j,'= morado, avanza hasta el final')
                return 4
            elif i//10 == 9:
                print(j,'= azul, inicio')
                return 1
        else:
            print(j)
        j+=1

def direccion2(list):#funcion de prueba
    j=0
    for i in list:
        if i !=0:
            if i%10 == 0:
                print(j,' up')
            elif i%10 ==1:
                print(j,'right')
            elif i%10 == 2:
                print(j,' left')
            elif i%10 == 3:
                print(j,' down')
        else:
            print(j)
        j+=1

def direccion(list,idx):
    i = list[idx] 
    if i !=0:
        if i%10 == 0:  
            return 0      
        elif i%10 ==1:    
            return 1      
        elif i%10 == 2: 
            return 2          
        elif i%10 == 3:
            return 3
    else:
        return 4   

def color(list,idx):
    i = list[idx]
    if i !=0:
        if i//10 == 1 or i//10 ==9:
            return 1
        elif i//10 ==2:
            return 2
        elif i//10 == 3:
            return 3
        elif i//10 == 4:
            return 4

   
def move(ruta,i):
    if direccion(ruta,i) == 0 and i > 4:
        i-=5        
    elif direccion(ruta,i) == 1 and i != 4 and i != 9 and i != 14 and i != 19 and i != 24:
        i+=1        
    elif direccion(ruta,i) == 2 and i != 0 and i != 5 and i != 10 and i != 15 and i != 20:
        i-=1        
    elif direccion(ruta,i) == 3 and i < 20:
        i+=5
    elif direccion(ruta,i) == 4 :
        print('CASILLA EN BLANCO, RUTA TERMINADA')
    else: 
        print('MOVIMIENTO NO PERMITIDO, FUERA DE RANGO')
    print(i)
    return i

def go(color):
    if color ==1:
        move()
    elif color ==2:
        print('esperar 5s')
        move()
    elif color ==3:
        print('activar disparo')
        move()
    elif color ==4:
        print('ir hasta el final')