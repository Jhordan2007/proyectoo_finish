from registrar_camper import *
from datos import *
from coordinador_config import *
from camper_config import *
from trainer_config import *

RUTA_DATOS_ESTUDIANTESEXP = "estudiantes_expulsados.json"
datos_estudiantes_expulsados = cargar_datos(RUTA_DATOS_ESTUDIANTESEXP)

RUTA_DATOS_ESTUDIANTESINSC = "estudiantes_inscritos.json"
datos_estudiantes_inscritos = cargar_datos(RUTA_DATOS_ESTUDIANTESINSC)

RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

def menu_menu():
  try:
    while True:
        print("----------------------------------------------------------------")
        print("Bievenido a la plataforma de campuslands")
        print("1. Registrarse")
        print("2. Ingresar como camper")
        print("3. Ingresar como trainer")
        print("4. ingresar como coordinador")
        print("0. salir")
        print("----------------------------------------------------------------")
        opc = int(input("Ingrese la opciòn que deseas--> "))
        if opc == 1:
          registrar_usuario(datos_estudiantes_inscritos)
          guardar_datos(datos_estudiantes_inscritos, RUTA_DATOS_ESTUDIANTESINSC)
        elif opc == 2:
          menu_camper()
        elif opc == 3:
          menu_trainer()
        elif opc == 4:
          menu_coordinador()
        elif opc == 0:
          print("has salido...")    
          break
  except Exception:
    print("hubo un error")
    menu_menu()