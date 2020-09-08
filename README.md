# Actualiza una carpeta que es respaldo de otra carpeta

### Script python para copiar en una carpeta de respaldo solo los archivos nuevos o modificados (Windows).

Este programa compara los archivos en la carpeta en la que se encuentra con los de otra carpeta que se quiere
respaldar. Si hay archivos nuevos o con una fecha de modificación más reciente en la carpeta
del sistema especificada, pregunta si puede proceder a copiarlos en la carpeta de respaldo.
**El script solo modifica la carpeta de respaldo y no elimina ningún archivo por seguridad.**

## Para usarlo:
  1. Descarga e instala el intérprete de [Python](https://www.python.org/) para Windows.
  2. [Descarga el código](https://github.com/oliver-almaraz/SincronizarRespaldo/archive/master.zip)
    y extrae el archivo *sincronizar.py* **en la carpeta que quieres usar como respaldo**.
  3. Abre el archivo *sincronizar.py* con el *Block de Notas* y edita la línea 16 con la ruta
    **de la carpeta que quieres respaldar**.
  4. La primera vez, copia todos los archivos de la carpeta que quieres respaldar en la carpeta de respaldo.
  5. Cuando quieras actualizar tu carpeta de respaldo, abre una ventana de Power Shell en la **carpeta de respaldo**:
  
      `Ctrl + Shift + Click Derecho (en un lugar vacío de la carpeta)`
      
      `'Abrir ventana de Power Shell aquí'`
      
  6. Para iniciar el programa, escribe en la ventana de Power Shell:
      ```shell
       python .\sincronizar.py
      ```
   ¡Listo! La póxima vez solo deberás presionar la tecla con la flecha hacia arriba de tu teclado y Power Shell
   volverá a escribir el último comando ejecutado ( `python .\sincronizar.py` )
