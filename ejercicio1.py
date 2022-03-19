import sys
#fecha1=19810807
#fecha2=20220806
fecha1=int(sys.argv[1])
fecha2=int(sys.argv[2])

def años_cumplidos(f1,f2):
    """Calcula el total de años cumplidos detallando años, meses y días exactos. Se asume la fecha 1 debe ser menor a la fecha 2
    args
    - f1 (entero) : la primer fecha en formato YYYYMMDD - Ejemplo: si quiere representar la fecha 07-08-1981 se expresaría como 19810708 
    - f2 (entero) : la segunda fecha en formato YYYYMMDD - normalmente sea la fecha actual
    """
    dia1=f1%100
    dia2=f2%100
    f1=f1//100
    f2//=100
    mes1=f1%100
    mes2=f2%100
    f1//=100
    f2//=100
    año1=f1
    año2=f2
    años=año1-año2-1
    if mes2<12 and mes2<mes1:
        mes2+=12
    meses=mes2-mes1

    if dia2<dia1:
        dia2+=31
    
    dias=dia2-dia1

    if dias>31:
        dias-=31
        if meses==11:
            meses=0
        else:
            meses+=1

    return "La persona tiene {} años {} meses {} dias".format(año2-año1-1,mes2-mes1,dia2-dia1)    

print (años_cumplidos(fecha1,fecha2))
