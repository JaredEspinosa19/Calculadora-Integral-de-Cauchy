import matplotlib.pyplot as plt
import math
import complex_number as z

def graphic_function(h,k,r1,z0,circle): #graficar unico numero 

    dis=math.sqrt(math.pow((h-z0.real),2) + math.pow((k-z0.imaginary),2))
    r=r1

    if dis>r:
        izda = min(-1, -abs(dis*2)-(abs(dis*2)*.3))
        dcha = max(1,abs(dis*2)+(abs(dis*2)*.3))
        abajo = min(-1, -abs(dis*2)-(abs(dis*2)*.3))
        arriba = max(1, abs(dis*2)+(abs(dis*2)*.3))
    else:
        izda = min(-1, -abs(r*2)-(abs(r*2)*.3))
        dcha = max(1,abs(r*2)+(abs(r*2)*.3))
        abajo = min(-1, -abs(r*2)-(abs(r*2)*.3))
        arriba = max(1, abs(r*2)+(abs(r*2)*.3))

    figure, axes = plt.subplots()
    draw_circle = plt.Circle((h, k), r,fill=False)

    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    plt.plot(z0.real,z0.imaginary,marker="o",color="red")
    # Pintamos lineas que pasan por el origen de coordenadas
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlim([izda,dcha])
    plt.ylim([abajo,arriba])
    plt.xlabel('Re(Z)')
    plt.ylabel('Im(Z)')
    title=(z.string_z("Z0=",z0)+"\n"+circle)
    plt.title(title)
    plt.show()