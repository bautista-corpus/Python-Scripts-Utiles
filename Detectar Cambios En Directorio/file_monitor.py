""" 
Script para detectar cambios en un directorio, especificamente para el
proyecto de ACR
Autor: Jesus Bautista
"""

import os
import time
import sys
import subprocess
from ftplib import FTP

ip_seeds = ["192.168.100.253","192.168.100.253","192.168.100.253","192.168.100.253"]

def listarArchivos():
    #Variable para la ruta al directorio
    path = './'
    #Lista vacia para incluir los ficheros
    lstFiles = []
    #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
    #Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            lstFiles.append(nombreFichero+extension)
            #print (nombreFichero+extension)           
    #print "longitud de la lista = ", len(lstFiles)
    return lstFiles

def send_part(files):
    print("Se envia el archivo\n")
    for file in files:
        file = file.split("_")
        if file[1] == "part1":
            send_to_peer(ip_seeds[0],file[0],file[1])
        elif file[1] == "part2":
            send_to_peer(ip_seeds[1],file[0],file[1])
        elif file[1] == "part3":
            send_to_peer(ip_seeds[2],file[0],file[1])
        elif file[1] == "part4":
            send_to_peer(ip_seeds[3],file[0],file[1])
        else:
            print("Desconocido")

def send_to_peer(ip,nombre_archivo,ext_parte):
    print("Enviando archivo > "+nombre_archivo+"_"+ext_parte+" al peer "+ip)
    ftp = FTP(ip) # Connect
    ftp.login("jesbta","jesbta") # Login
    file = open("./"+nombre_archivo+"_"+ext_parte,'rb') # Abre archivo local
    stor_no_local = "STOR "+nombre_archivo+"."+ext_parte
    ftp.storbinary(stor_no_local,file) # Upload
    ftp.retrlines('LIST') # Lista archivos
    ftp.quit()
    print("\n")

if __name__ == "__main__":
    listaAnterior = listarArchivos()
    listaActual = listarArchivos()
    comparacion = []
    nuevos = []
    while(1):
        for archivo in listaActual:
            print(archivo)
        if len(listaAnterior)==len(listaActual):
            print("No hay cambios\n")
        else:
            print("Hay cambios\n")
            for item in listaActual:
                if item in listaAnterior:
                    comparacion.append(item)
                else:
                    nuevos.append(item)
            print(str(len(nuevos))+" nuevos archivos >")
            print(nuevos)
            print("\n")
            send_part(nuevos)
        listaAnterior = listaActual
        listaActual = listarArchivos()
        nuevo = []
        time.sleep(4)
