from datos import *

RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

def menu_trainer():
    try:
        while True:
            print("----------------------------------------------------------------")
            print("Bienvenido al menu Trainer")
            print("1. Para ingresar a tu perfil como trainer: ")
            print("2. Para premiar a estudia")
            print("0. Salir ")
            print("----------------------------------------------------------------")
            opc = int(input("Ingrese la opciòn que deseas--> "))
            if opc == 1:
                submenu_trainer(datos_estudiantes_Cursando)
            if opc == 2:
                premio(datos_estudiantes_Cursando)
            if opc == 0:
                break
    except Exception:
        print("hubo un error")

def premio(datos_estudiantes_Cursando):
     try:
        while True:
                ruta=input("ingresa la ruta contraseña a la que deseas entrar: ").lower()
                for i in datos_estudiantes_Cursando:
                    print(i)
                    if ruta == i:
                        print(f"perfil de {i} ")
                        print(f"Estudiantes {datos_estudiantes_Cursando[i]}")
                doc = input("ingresa el documento del estudiante que deseas asignarle las notas: ")
                for o in range(len(ruta)):
                    if doc == datos_estudiantes_Cursando[ruta][o]["documento"]:
                        print("Tu nota teorica es: ", datos_estudiantes_Cursando[ruta][o]["nota1"])
                        print("Tu nota de pratica es: ", datos_estudiantes_Cursando[ruta][o]["nota2"])
                        print("Tu nota final es: ", datos_estudiantes_Cursando[ruta][o]["notaf"])
                        print(datos_estudiantes_Cursando[ruta][o]["estrellas"])
                        datos_estudiantes_Cursando[ruta][o]["estrellas"]=input("Ingresa las estrellas que deseas agregarle. ESTRELLA-->*")
                        guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS)
                        break
     except Exception:
        print("Hubo un error")
def submenu_trainer(datos_estudiantes_Cursando):
    try:
        while True:
            ruta=input("ingresa la ruta contraseña a la que deseas entrar: ").lower()
            for i in datos_estudiantes_Cursando:
                print(i)
                if ruta == i:
                    print(f"perfil de {i} ")
                    print(f"Estudiantes {datos_estudiantes_Cursando[i]}")
            doc = input("ingresa el documento del estudiante que deseas asignarle las notas: ")
            for o in range(len(ruta)):
                if doc == datos_estudiantes_Cursando[ruta][o]["documento"]:
                    datos_estudiantes_Cursando[ruta][o]["nota1"] = int(input(" ingresa la nota que deseas asignarle en teoria: "))
                    datos_estudiantes_Cursando[ruta][o]["nota2"] = int(input(" ingresa la nota que deseas asignarle en pratica: "))
                    datos_estudiantes_Cursando[ruta][o]["notaf"] = (datos_estudiantes_Cursando[ruta][o]["nota1"] + datos_estudiantes_Cursando[ruta][o]["nota2"]) / 2
                guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS)
            break
    except Exception:
        print("hubo un error ")