import glob
"""
glob.glob es una función en Python que se utiliza para 
encontrar todos los nombres de archivo que 
coinciden con un patrón específico según 
las reglas de coincidencia de nombres 
de archivos de Unix. 
Esta función es parte del módulo 
glob estándar de Python."""
myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath,'r') as file:
        print(file.read().upper())
