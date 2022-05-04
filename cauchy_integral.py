import complex_number as z
import math

def evaluation_number(h,k,r,z0):
    distance=math.sqrt(math.pow((h-z0.real),2) + math.pow((k-z0.imaginary),2))
    if distance<r: 
        return -1
    elif distance == math.sqrt(r):
        return 0
    else:
        return 1

def cte(c):
    aux=z.Complex_Number(0,2*math.pi)
    result=z.Complex_Number(0,0)
    result.multiplicar(c,aux)
    return result

def z_n(z0,n):
    aux=z.Complex_Number(0,0)
    aux.potencia(z0,n)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux)
    return result

def e_z(z0):
    aux=z.Complex_Number(0,0)
    aux.exponencial(z0)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux)
    return result

def z_2(z0):
    aux1=z.Complex_Number(0,0)
    aux1.potencia(z0,2)
    aux2=z.Complex_Number(0,0)
    aux2.suma(z.Complex_Number(0,1),aux1)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux2)
    return result

def sen(z0):
    aux=z.Complex_Number(0,0)
    aux.seno(z0)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux)
    return result

def cos(z0):
    aux=z.Complex_Number(0,0)
    aux.coseno(z0)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux)
    return result

def cosh(z0):
    aux=z.Complex_Number(0,0)
    aux.cosenoh(z0)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux)
    return result

def senh(z0):
    aux=z.Complex_Number(0,0)
    aux.senoh(z0)
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(0,2*math.pi),aux)
    return result