# se coloca doble pleca para que lo cuente como caracter especial
#agregamos otra ubicacion llamada datos.txt que nos va mandar un error por que no existe
# la 'r' es para leer 
# 'w' write para rehacer
# 'a' append para agregar

try: 
    mi_ruta = "C:\\Users\\labc113\\Documents\\uam\\ejercicio\\" #Mas ordenado dar un valor a la ubicacion
    mi_archivo = open(mi_ruta+'datos.txt', 'r') #De aqui testear las funciones anteriores
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no existe")

#en el archivo txt no escribir txt por que no lo va encontrar