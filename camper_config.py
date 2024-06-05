#DOCUMENTO PARA EL PERFIL CAMPER
import json
from datos import *
RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)
#Esta funcion permite mostrar el perfil del estudiante
def mostrar_perfil(datos_estudiantes_Cursando):
    try:
        doc= input("Ingrese el numero del documento del usuario") #pide el documento y lo almacena en una variable 
        for o in datos_estudiantes_Cursando:  #Recorre el json datos estudiantes cursando para mostrar las rutas que hay
            print(f"-->{o}") #escribe las rutas que hay en el momento
        ruta = input("A que ruta pertenece? ").lower() #Pide la ruta a la cual pertenece y la almacena en una variable
        for u in range(len(datos_estudiantes_Cursando[ruta])):  # recorre las rutas que hay y las va almacenando en u 
            if doc == datos_estudiantes_Cursando[ruta][u]["documento"]:#Valida si el documento esta en el archivo de datos estudiantes cursando en la ruta que se pidio y en la posicion de documento
                print("usuario encontrado", datos_estudiantes_Cursando[ruta][u]) #Muestra el perfil del esuario con ese documento
            else:
                print("no esite") #si no existe el usuario nos vota esto
    except Exception:
        print("hubo un error")
#Mostrar las notas del estudiante
def mostrar_notas(datos_estudiantes_Cursando):
    try:
        doc= input("Ingrese el numero del documento del usuario") #pide el documento y lo almacena en una variable 
        for o in datos_estudiantes_Cursando: #Recorre el json datos estudiantes cursando para mostrar las rutas que hay
            print(f"-->{o}") #escribe las rutas que hay en el momento
        ruta = input("A que ruta pertenece?").lower() #Pide la ruta a la cual pertenece y la almacena en una variable
        for u in range(len(datos_estudiantes_Cursando[ruta])): # recorre las rutas que hay y las va almacenando en u 
            if doc in datos_estudiantes_Cursando[ruta][u]["documento"]: #Valida si el documento esta en el archivo de datos estudiantes cursando en la ruta que se pidio y en la posicion de documento
                print("Tu nota teorica es: ", datos_estudiantes_Cursando[ruta][u]["nota1"]) # Muestra la nota 1 del estudiante 
                print("Tu nota de pratica es: ", datos_estudiantes_Cursando[ruta][u]["nota2"]) # Muestra la nota 2 del estudiante
            else: 
                print("documento o ruta equivocada") # Dice que escribio algo mal.
    except Exception:
        print("hubo un error") # No deja que se acabe el programa cuando haya un error 
def menu_camper():
    try:
        while True: #Menu del camper y sus opciones
            print("----------------------------------------------------------------")
            print("Bienvenido al menu camper")
            print("1. Mostrar perfil")
            print("2. Mostrar notas")
            print("0. salir")
            print("----------------------------------------------------------------")
            opc = int(input("Ingrese la opciòn que deseas--> ")) #Nos permite almacenar la opcion que desea seleccionar en numeros
            if opc == 1:
                mostrar_perfil(datos_estudiantes_Cursando)
            elif opc == 2:
                mostrar_notas(datos_estudiantes_Cursando)
            elif opc == 0:
                break
    except Exception:
        print("hubo un error")
