import json
from datos import *
RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

def mostrar_perfil(datos_estudiantes_Cursando):
    try:
        doc= input("Ingrese el numero del documento del usuario")
        for o in datos_estudiantes_Cursando:
            print(f"-->{o}")
        ruta = input("A que ruta pertenece? ").lower()
        for u in range(len(datos_estudiantes_Cursando[ruta])):
            if doc == datos_estudiantes_Cursando[ruta][u]["documento"]:
                print("usuario encontrado", datos_estudiantes_Cursando[ruta][u])
            else:
                print("no esite")
    except Exception:
        print("hubo un error")

def mostrar_notas(datos_estudiantes_Cursando):
    try:
        doc= input("Ingrese el numero del documento del usuario")
        for o in datos_estudiantes_Cursando:
            print(f"-->{o}")
        ruta = input("A que ruta pertenece?").lower()
        for u in range(len(datos_estudiantes_Cursando[ruta])):
            if doc in datos_estudiantes_Cursando[ruta][u]["documento"]:
                print("Tu nota teorica es: ", datos_estudiantes_Cursando[ruta][u]["nota1"])
                print("Tu nota de pratica es: ", datos_estudiantes_Cursando[ruta][u]["nota2"])
            else: 
                print("documento o ruta equivocada")
    except Exception:
        print("hubo un error")
def menu_camper():
    try:
        while True:
            print("----------------------------------------------------------------")
            print("Bienvenido al menu camper")
            print("1. Mostrar perfil")
            print("2. Mostrar notas")
            print("0. salir")
            print("----------------------------------------------------------------")
            opc = int(input("Ingrese la opciòn que deseas--> "))
            if opc == 1:
                mostrar_perfil(datos_estudiantes_Cursando)
            elif opc == 2:
                mostrar_notas(datos_estudiantes_Cursando)
            elif opc == 0:
                break
    except Exception:
        print("hubo un error")