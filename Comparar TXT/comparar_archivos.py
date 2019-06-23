def comparar_archivos(file1,file2):
    linum=0
    numdif=0
    print("\nComparando " + file1 + " ::: " + file2)
    with open(file1, 'r') as file1:
        with open(file2, 'r') as file2:
            with open ("diff.txt", "w") as out_file:
                f2_lines = set(file2)
                for line in file1:
                    linum+=1
                    if line not in f2_lines:
                        numdif+=1
                        print("Diferencia en la linea: "+str(linum))
                        out_file.write(str(linum)+": "+line)
    print("\nNumero de diferencias: "+str(numdif))
    print("Archivo diff.txt creado")

if __name__ == "__main__":
    print("Programa para comparar dos archivos de texto")
    comparar_archivos("file1.txt","file2.txt")