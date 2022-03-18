def invertirDigitos(numero,p1,p2):
    val1 = 0
    val2 = 0
    cont = 0
    num=numero
    while(num>0):
        cont += 1
        num = num//10
    num=numero
    cont2 = 0
    resultado = 0
    while(cont>0):
        digito=num%10
        if(cont==p1):
            val1=digito
        elif(cont==p2):
            val2=digito
        cont2+=1
        num=num//10
        cont-=1
    num=numero
    cont3 = 0
    while(cont2>0):
        digito=num%10
        if(cont2==p1):
            resultado = resultado + (val2*10**cont3)
        elif(cont2==p2):
            resultado = resultado + (val1*10**cont3)
        else:
            resultado = resultado + (digito*10**cont3)
        cont3+=1
        num=num//10
        cont2-=1
    return(resultado)
print(invertirDigitos(1230,1,4))