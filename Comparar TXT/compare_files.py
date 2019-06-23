def comparar_archivos(file1,file2):
    linum=0
    numdif=0
    aux=0
    print("\nComparando " + file1 + " ::: " + file2)
    with open(file1, 'r') as file1:
        lineas_file1 = [linea.split("\n") for linea in file1]
    with open(file2, 'r') as file2:
        lineas_file2 = [linea.split("\n") for linea in file2]
    with open ("diff.txt", "w") as out_file:
        try:
            for line in lineas_file1:
                if (line == lineas_file2[linum]):
                    aux+=1
                else:
                    numdif+=1
                    print("Diferencia en la linea: "+str(linum))
                    out_file.write(str(linum)+": "+str(line)+" --> "+str(lineas_file2[linum])+"\n")
                linum+=1
        except IndexError as error:
            print("El numero de lineas entre los archivos es diferente")
        
    if numdif == 0:
        print("\nLos archivos son iguales\n")
    else:
        print("\nNumero de diferencias: "+str(numdif)) 

    print("Archivo diff.txt creado")

if __name__ == "__main__":
    print("Programa para comparar dos archivos de texto")
    comparar_archivos("R2sc","R3sc")