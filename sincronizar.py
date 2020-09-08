############################################################################
# Script que compara la carpeta en la que se encuentra con la otra carpeta
# especificada para comparar sus contenidos y la fecha de modificación de
# sus archivos. Posteriormente, pregunta si se quiere actualizar la carpeta
# de respaldos (donde se debe encontrar este script) con los archivos nuevos
# o con archivos que tienen una fecha de modificación más reciente en la
# carpeta del sistema.
############################################################################

# Crado por Oliver Almaraz el 06-09-2020
# oliver.almaraz@gmail.com
# Última modificación: 07-09-2020


# Si quieres CAMBIAR EL DIRECTORIO a respaldar reemplaza el valor de 'path'
# (ten cuidado de escribir la ruta correctamente y entre comillas, no debe
# terminar con '\' y no borres la 'r' que está antes de las comillas):

path = r"C:\Users\fulano\Documentos\Carpeta de ejemplo"

#######################################################################
##### Fin del encabezado, no modifiques nada debajo de esta línea #####
#######################################################################

import os
from datetime import datetime
from shutil import copyfile
from pathlib import Path

respaldo = {}
sistema = {}

nuevos = {}
masRecientes = {}

def ls(directorio, dict):
    """
    Añade a un diccionario la ruta absoluta de cada archivo en
    el directorio especificado con su timestamp como valor.
    """
    for root, dirs, files in os.walk(directorio):
        for filename in files:
            rutaAbsol = str(root+'\\'+filename).replace("\\ ", " ")
            if filename == "sincronizar.py":
						#Se ignora este script
                continue
            try:
                modif = os.path.getmtime(rutaAbsol)
            except OSError:
                try:
# Si el archivo no ha sido modificado se muestra la fecha de creación
                    modif = os.path.getctime(rutaAbsol)
                except OSError:
# Si aún así Windows no encuentra una fecha válida
                    modif = 0
# Cada archivo se almacena en un diccionario junto con su timestamp
            dict[rutaAbsol]=modif

def copiarRemplazar(dictio):
    """
    Toma un diccionario (que contiene archivos a copiar)
    y copia cada uno de los archivos en la carpeta donde
    se encuentra este script. Si no existen las subcarpetas
    las crea.
    """
    for ruta, nombre in dictio.items():
        print("copiando '",nombre,"'")
        relativePath = (str(ruta.replace(path,".")))
        separarNombreDeRuta = nombre.split("\\")
	# Para crear las subcarpetas se quita el nombre del archivo de la ruta
        nombreSolo = str(separarNombreDeRuta[-1])
        Path(relativePath.replace(nombreSolo,"")).mkdir(parents=True, exist_ok=True)
	#se crean las subcarpetas si no existen
        copyfile(ruta, relativePath)

print()
print("Importante: verifica que este programa esté en la carpeta que quieres usar como respaldo.")
print()

# Se verifica si la ruta (línea 16) sigue siendo válida
isdir = os.path.isdir(path)
if isdir != True or path[-1] == "\\":
	print("""
La ruta especificada en este script no es válida o no existe.
Abre este script ('sincronizar.py') con un editor de texto
(como el Block de Notas) y actualiza la ruta en la línea 16.
Si quieres salir, presiona simultáneamente Ctrl + c
""")

# Si el path en el script es correcto, de todos modos se confirma que sea el deseado
else:
	print("El directorio que quieres respaldar en esta carpeta está configurado como ", path)

cambiarPath = input("¿Quieres CAMBIAR la ruta solo por esta ocasión? (s/n) ")
if cambiarPath.lower() == "s":
    print("Ingresa la ruta del directorio que quieres respaldar en esta carpeta") 
    print(r"(ejemplo: C:\Users\fulano\Documentos\Carpeta de prueba ).")
    print("""
Escribe la ruta o pégala con Ctrl + Shift + v:
""")
    path = input()

# La ruta debe ser válida para poder continuar
isdir = os.path.isdir(path)
while isdir != True or path[-1] == "\\": # Si la nueva ruta no es válida
    print()
    path = input("La ruta especificada no existe o está mal escrita, prueba otra vez:")
    isdir = os.path.isdir(path)
print()
print("Procesando...")
print()

ls(".", respaldo) # Se crea el diccionario con los archivos en esta carpeta de respaldo.
ls(path, sistema) # Se crea el diccionario con los archivos en la carpeta a respaldar.


print("Archivos en la carpeta del sistema que no existen en la carpeta de respaldo:")
print()
for rutaAbsol,modif in sistema.items():
# Se iguala la ruta absoluta del archivo con la ruta relativa de los respaldos.
    if rutaAbsol.replace(str(path+"\\"), ".\\") not in respaldo:
        if modif != 0:
            fechaHumanaConDecimales = str(datetime.fromtimestamp(modif))
            fechaHumana = fechaHumanaConDecimales[:19]
            print(fechaHumana,"    ",rutaAbsol)
        else:
            print("sin fecha","         ",rutaAbsol)
        nuevos[rutaAbsol] = rutaAbsol.replace(str(path+"\\"), "")
print()

print("Archivos que son más recientes en la carpeta del sistema:")
print()

for rutaAbsol,modif in sistema.items():
    if rutaAbsol.replace(str(path+"\\"), ".\\") in respaldo:
        if modif > respaldo[rutaAbsol.replace(str(path+"\\"), ".\\")]:
            if modif != 0: # la ruta relativa de los respaldos.
                fechaHumanaConDecimales = str(datetime.fromtimestamp(modif))
                fechaHumana = fechaHumanaConDecimales[:19]
                print(fechaHumana,"    ",rutaAbsol)
            else:
                print("sin fecha","         ",rutaAbsol)
            masRecientes[rutaAbsol] = rutaAbsol.replace(str(path+"\\"), "")
            #Se guarda en un nuevo diccionario la ruta absoluta y el nombre del archivo.
print()

if len(nuevos) >= 1:
    pullNew = input("¿Añadir a esta carpeta de respaldo los archivos nuevos en el sistema? (s/n)")
    if pullNew.lower() == "s":
        print()
        copiarRemplazar(nuevos)
        print()
else:
    print("No hay archivos nuevos que agregar.")
    print()

if len(masRecientes) >= 1:
    pullRecent = input("¿Actualizar los archivos obsoletos en el respaldo? (s/n)")
    if pullRecent.lower() == "s":
        print()
        copiarRemplazar(masRecientes)
else:
    print()
    print("No hay archivos obsoletos que actualizar.")

print()
print("Actualización terminada.")
print()