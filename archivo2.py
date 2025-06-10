
try:
    mi_ruta = 'C:\\Users\\labc113\\Documents\\uam\\ejercicio\\'
    
    mi_archivo=open(mi_ruta + "notas.txt", 'w')
    texto=input("Dime algo: ")
    mi_archivo.write(texto)
    mi_archivo.close()

except Exception:

    print("Error")