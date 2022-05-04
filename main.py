import complex_number as z
import graphic as gp
import cauchy_integral as ci
import generalizared_cauchy_integral as gci
import os

def main():
    #Solicitar datos
    print("Inserte la circunferencia de la forma (x-h)^2 + (y-k)^2 = r")
    h=int(input("Inserte el valor de h: "))
    k=int(input("Inserte el valor de k: "))
    r=int(input("Inserte el valor de r: "))

    Z0=z.entrada_usuario(input("Digite el numero Z0 de la forma 'a+bi': "))

    print("Seleccione la función por la que se evaluará la integral de Cauchy")
    function=int(input("1- Cte \n2- z^m \n3- e^z \n4- z^2 + i \n5- sen(z) \n6- cosh(z) "))
    if function==1:
        cte=z.entrada_usuario(input("Introduzca el valor de la función cte:"))
    elif function==2:
        z_n=int(input("Digite la potencia de la función z^m: "))
    
    n=int(input("Digite la potencia de la integral de Cauchy: "))
    os.system("cls")

    #Confirmacion de datos
    if h>=0 and k>=0: #- -
        print("λ=(x-{})^2 + (y-{})^2 = {}".format(abs(h),abs(k),r))
        circle="λ=(x-{})^2 + (y-{})^2 = {}".format(abs(h),abs(k),r)
    elif h<0 and k>=0: #+ -
        print("λ=(x+{})^2 + (y-{})^2 = {}".format(abs(h),abs(k),r))
        circle="λ=(x+{})^2 + (y-{})^2 = {}".format(abs(h),abs(k),r)
    elif h>=0 and k<0:#- +
        print("λ=(x-{})^2 + (y+{})^2 = {}".format(abs(h),abs(k),r))
        circle="λ=(x-{})^2 + (y+{})^2 = {}".format(abs(h),abs(k),r)
    else:#+ +
        print("λ=(x+{})^2 + (y+{})^2 = {}".format(abs(h),abs(k),r))    
        circle="λ=(x+{})^2 + (y+{})^2 = {}".format(abs(h),abs(k),r)

    print(z.string_z("Z0 = ",Z0))
    if  function==1:
        print("f(z)="+ z.string_z("",cte))
    elif function==2:
        print("f(z)= z^{}".format(z_n))
    elif function==3:
        print("f(z)= e^z")
    elif function==4:
        print("f(z)= z^2 + i")
    elif function==5:
        print("f(z)= sen(z)")
    else:
        print("f(z)= cosh(z)")
    print("n = {}".format(n))
    
    if ci.evaluation_number(h,k,r,Z0)==1:#afuera de la función
        print("Integral de Cauchy= "+ z.string_z("",z.Complex_Number(0,0)))
        print("Integral de Cauchy generalizada= "+ z.string_z("",z.Complex_Number(0,0)))
        gp.graphic_function(h,k,r,Z0,circle)
        exit()
        pass
    elif ci.evaluation_number(h,k,r,Z0)==0: #sobre contorno función
        print("La integral de cauchy está indefinida por que Z0 se encuentra sobre el contorno de la función lambda")
        gp.graphic_function(h,k,r,Z0,circle)   
        exit()
    else:
        if  function==1: #cte
            print("Integral de Cauchy= "+ z.string_z("",ci.cte(cte)))
            print("Integral de Cauchy generalizada= "+ z.string_z("",gci.cte(Z0,cte,n)))
        elif function==2: #z^n
            print("Integral de Cauchy= "+ z.string_z("",ci.z_n(Z0,z_n)))
            print("Integral de Cauchy generalizada= "+ z.string_z("",gci.z_n(Z0,z_n,n)))
        elif function==3: #e^z
            print("Integral de Cauchy= "+ z.string_z("",ci.e_z(Z0)))
            print("Integral de Cauchy generalizada= "+ z.string_z("",gci.e_z(Z0,n)))
        elif function==4: #z^2+i
            print("Integral de Cauchy= "+ z.string_z("",ci.z_2(Z0)))
            print("Integral de Cauchy generalizada= "+ z.string_z("",gci.z_2(Z0,n)))
        elif function==5: #sen(z)
            print("Integral de Cauchy= "+ z.string_z("",ci.sen(Z0)))
            print("Integral de Cauchy generalizada= "+ z.string_z("",gci.sen(Z0,n)))
        else: #cosh(z)
            print("Integral de Cauchy= "+ z.string_z("",ci.cosh(Z0)))
            print("Integral de Cauchy generalizada= "+ z.string_z("",gci.cosh(Z0,n)))
    gp.graphic_function(h,k,r,Z0,circle) 

if __name__ == "__main__":
    main()