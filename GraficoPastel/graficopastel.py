from pylab import *

def graficar(label,dato):
    aux = 100 - dato
    y = [dato,aux]
    pie(y)
    title(label)
    #legend( ('Etiqueta1',), loc = 'upper left')
    draw()
    axis('equal')
    nombrearchivo = label + ".png"
    savefig(nombrearchivo,dpi=50)
    close()
    grid(True)
    #show()