import complex_number as z
import cauchy_integral as ci
import math

def cte(z0,c,n):
    if n==1:
        return ci.cte(c)
    else:
        return z.Complex_Number(0,0)

def z_n(z0,z_n,n):
    if z_n<0:
        n_d=1
        for x in range(1,n):
            n_d=n_d*z_n
            z_n-=1
            
        aux=z.Complex_Number(0,0)
        aux.multiplicar(z.Complex_Number(n_d,0),ci.z_n(z0,z_n))
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),aux)
        return result
    elif z_n==0:
        if n==1:
            result=z.Complex_Number(0,0)
            result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.z_n(z0,0))
            return result
        else:
            return z.Complex_Number(0,0)
    else:
        if n==1:
            return ci.z_n(z0,z_n)
        else:
            n_d=1
            for x in range(1,n):
                n_d=n_d*z_n
                z_n-=1
            
            if(z_n<0):
                z_n=0
                

            aux=z.Complex_Number(0,0)
            aux.multiplicar(z.Complex_Number(n_d,0),ci.z_n(z0,z_n))
            result=z.Complex_Number(0,0)
            result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),aux)
            return result

def e_z(z0,n):
    result=z.Complex_Number(0,0)
    result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.e_z(z0))
    return result

def z_2(z0,n):
    if n==1:
        return ci.z_2(z0)
    elif n==2:
        aux=z.Complex_Number(0,0)
        aux.multiplicar(z.Complex_Number(2,0),z0)
        aux1=z.Complex_Number(0,0)
        aux1.multiplicar(z.Complex_Number(0,2*math.pi),aux)
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),aux1)
        return result
    elif n==3:
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.cte(2))
        return result
    elif n>3:
        return z.Complex_Number(0,0)

def sen(z0,n):
    if n%4==1: #sen
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.sen(z0))
        return result
    elif n%4==2: #cos
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.cos(z0))
        return result
    elif n%4==3: #-sen
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(-(1/(math.factorial(n-1))),0),ci.sen(z0))
        return result
    elif n%4==0: #-cos
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(-(1/(math.factorial(n-1))),0),ci.cos(z0))
        return result

def cosh(z0,n):
    if n%2==0: #1,3,5 sen
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.senh(z0))
        return result
    elif n%2==1: #0,2,4,5 cose
        result=z.Complex_Number(0,0)
        result.multiplicar(z.Complex_Number(1/(math.factorial(n-1)),0),ci.cosh(z0))
        return result