"""Diario Personal"""

import datetime 

ahora= datetime.datetime.now()

try:
    mi_ruta = 'C:\\Users\\labc205\\Desktop\\UAM\\IntProgG2-semana12\\notas\\'
    
    mi_archivo=open(mi_ruta + "diario.txt", "a")
    bienvenida=("Bienvenido a tu diario personal")
    fecha = f"Fecha de ingreso de hoy: {ahora.strftime('%d/%m/%Y')}\n"
    texto=input("Empieza a escribir: ")
    mi_archivo.write(bienvenida)
    mi_archivo.write("\n")
    mi_archivo.write(fecha)
    mi_archivo.write("\n")
    mi_archivo.write(texto)
    mi_archivo.close()  
    print("fin")

except Exception:

    print("Error")