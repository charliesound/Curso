def pedirAno():
    Año = input("¿Que Año es?: ")
    while validaAno(Año) == False:
        print ("Año Invalido escribelo en numero")
        Año = input("¿Que Año es? en numero: ")
    return int(Año)

def validaAno(cadena):
    try:
        n = int(cadena)
        if n>=0:
            return True
        
        return False
    except:
        return False

def esBisiesto(Año):
    if Año % 4 == 0 and Año % 100 != 0 or Año % 400 == 0:
        print('El año es bisiesto')
    else:
        print('El año no es bisiesto')
        
Año = pedirAno()    
pedirAno = esBisiesto(Año)

        
   

