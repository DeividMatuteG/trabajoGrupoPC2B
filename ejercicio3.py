clave=0
tam=0
def cifrar(num):
    global clave
    global tam
    suma=0
    n=num
    while(n>0):
        suma+=(n%10)
        n//=10
        tam+=1
    clave=suma%10
    nuevoNum=0
    numero=num
    exponente=0
    while(numero>0):
        ultimo=numero%10
        numero//=10
        nuevoNum+=((ultimo+clave)%10)*(10**exponente)
        exponente+=1
    descifrado=nuevoNum*10+clave
    divisor=1*10**(exponente+1)
    resultado=descifrado/divisor
    return(resultado)
print("Clave cifrada:",cifrar(77635245))
def descifrar(numCifrado):
    global tam
    numero=0
    primero = int(numCifrado*10)
    numero=int(numCifrado*10**(tam))
    n_descifrado=0
    while(tam!=0):
        if(primero!=0):
            num=int(numero/10**(tam-1))
            numero=numero-(num*10**(tam-1))
            if(num-clave)<0:
                n_descifrado+=(10+num-clave)*10**(tam-1)
            else:
                n_descifrado+=(num-clave)*10**(tam-1)
        else:
            n_descifrado+=(10-clave)*10**(tam-1)
            primero=1
        tam-=1
    return n_descifrado
print("Clave descifrada:",descifrar(0.665241349))