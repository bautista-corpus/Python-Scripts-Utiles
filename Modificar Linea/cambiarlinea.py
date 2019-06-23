def modificar_dato(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila-1].split(';')
            columnas[columna] = nuevo_dato
            contenido[fila-1] = ';'.join(columnas)+ '\n'
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)
    return 1


"""Aqui empieza el programa"""
print("Se va a modificar el archivo\n")
if(modificar_dato('fichero', [1,2,5], 6, 'N')):
    print("El archivo se modifico sin errores\n")
else:
    print("El archivo no se pudo modificar correctamente\n")

print("El programa finalizo")