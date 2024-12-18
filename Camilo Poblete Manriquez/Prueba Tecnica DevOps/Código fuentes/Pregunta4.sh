#!/bin/bash

# Descripción y ejemplo de uso de los comandos

echo "Descripción y ejemplos de uso de comandos en Linux"

# Comando: cat
echo "Comando: cat"
echo "Descripción: El comando 'cat' se utiliza para concatenar y mostrar el contenido de archivos."
echo "Ejemplo de uso:"
echo "cat archivo.txt"
echo "Salida (contenido del archivo):"
echo "Este es el contenido del archivo."

# Comando: ps
echo "Comando: ps"
echo "Descripción: El comando 'ps' muestra una instantánea de los procesos actuales en el sistema."
echo "Ejemplo de uso:"
echo "ps aux | head -5"
echo "Salida (primeros 5 procesos en el sistema):"
ps aux | head -5

# Comando: grep
echo "Comando: grep"
echo "Descripción: El comando 'grep' se utiliza para buscar texto dentro de archivos o la salida de otros comandos."
echo "Ejemplo de uso:"
echo "grep 'cadena' archivo.txt"
echo "Salida (líneas que contienen 'cadena' en el archivo):"
echo "Esta es una cadena de ejemplo."

# Comando: tail
echo "Comando: tail"
echo "Descripción: El comando 'tail' muestra las últimas líneas de un archivo."
echo "Ejemplo de uso:"
echo "tail -n 10 archivo.log"
echo "Salida (últimas 10 líneas del archivo log):"
echo "2024-12-18 21:47:34 - Ejemplo de última línea del archivo log."