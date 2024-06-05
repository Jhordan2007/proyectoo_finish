import json #IMPORTAMOS O TRAEMOS PARA PODER TOMAR LOS JSON QUE NECESITEMOS
from datos import * #Importamos los datos de cargar_datos y guardar_datos
from registrar_camper import* #importamos el registrar_camper que es donde esta las funciones para reigstrar al camper 
RUTA_DATOS_ESTUDIANTESEXP = "estudiantes_expulsados.json"
datos_estudiantes_expulsados = cargar_datos(RUTA_DATOS_ESTUDIANTESEXP)

RUTA_DATOS_ESTUDIANTESCOND = "estudiantes_condicionales.json"
datos_estudiantes_condicionales = cargar_datos(RUTA_DATOS_ESTUDIANTESCOND)


RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

RUTA_DATOS_ESTUDIANTESINSC = "estudiantes_inscritos.json"
datos_estudiantes_inscritos = cargar_datos(RUTA_DATOS_ESTUDIANTESINSC)



def Aprobo_o_no(datos_estudiantes_Cursando):
    try:
        doc= input("Ingrese el numero del documento del usuario")
        for o in datos_estudiantes_Cursando:
            print(f"-->{o}")
        ruta = input("A que ruta pertenece?").lower()
        for u in range(len(datos_estudiantes_Cursando[ruta])):
            print("la nota definitiva de estudiante es: ",datos_estudiantes_Cursando[ruta][u]["notaf"])
            if doc  == datos_estudiantes_Cursando[ruta][u]["documento"]:
                print("usuario encontrado")
                test = input("Desea aprobarlo, condicional, no aprobarlo? [Si][Condicional][No]").lower()
                if test == "no":
                    for i in range(len(datos_estudiantes_Cursando[ruta])):
                        if datos_estudiantes_Cursando[ruta][i]["documento"]== doc:
                            usuario = {}            
                            usuario["nombres"] = datos_estudiantes_Cursando[ruta][i]["nombres"]
                            usuario["documento"] = datos_estudiantes_Cursando[ruta][i]["documento"]
                            usuario["Apellidos"] = datos_estudiantes_Cursando[ruta][i]["Apellidos"]
                            usuario["direccion"] = datos_estudiantes_Cursando[ruta][i]["direccion"]
                            usuario["Edad"] = datos_estudiantes_Cursando[ruta][i]["Edad"]
                            usuario["Acudiente"] = datos_estudiantes_Cursando[ruta][i]["Acudiente"]
                            usuario["celular"] = datos_estudiantes_Cursando[ruta][i]["celular"]
                            usuario["telefono"] = datos_estudiantes_Cursando[ruta][i]["telefono"]
                            usuario["estado"] = "expulsado"
                            usuario["riesgo"] = datos_estudiantes_Cursando[ruta][i]["riesgo"]
                            usuario["nota1"] = datos_estudiantes_Cursando[ruta][i]["nota1"]
                            usuario["nota2"] = datos_estudiantes_Cursando[ruta][i]["nota2"]
                            datos_estudiantes_expulsados["expulsados"].append(usuario)
                            datos_estudiantes_Cursando[ruta].pop(i)
                if test == "condicional":
                    for i in range(len(datos_estudiantes_Cursando[ruta])):
                        if datos_estudiantes_Cursando[ruta][i]["documento"]== doc:
                            usuario = {}            
                            usuario["nombres"] = datos_estudiantes_Cursando[ruta][i]["nombres"]
                            usuario["documento"] = datos_estudiantes_Cursando[ruta][i]["documento"]
                            usuario["Apellidos"] = datos_estudiantes_Cursando[ruta][i]["Apellidos"]
                            usuario["direccion"] = datos_estudiantes_Cursando[ruta][i]["direccion"]
                            usuario["Edad"] = datos_estudiantes_Cursando[ruta][i]["Edad"]
                            usuario["Acudiente"] = datos_estudiantes_Cursando[ruta][i]["Acudiente"]
                            usuario["celular"] = datos_estudiantes_Cursando[ruta][i]["celular"]
                            usuario["telefono"] = datos_estudiantes_Cursando[ruta][i]["telefono"]
                            usuario["estado"] = "condicional"
                            usuario["riesgo"] = True
                            usuario["nota1"] = datos_estudiantes_Cursando[ruta][i]["nota1"]
                            usuario["nota2"] = datos_estudiantes_Cursando[ruta][i]["nota2"]
                            datos_estudiantes_condicionales["condicionales"].append(usuario)
                            datos_estudiantes_Cursando[ruta].pop(i)
                guardar_datos(datos_estudiantes_Cursando, RUTA_DATOS_ESTUDIANTESCURS)
                guardar_datos(datos_estudiantes_expulsados, RUTA_DATOS_ESTUDIANTESEXP)
                guardar_datos(datos_estudiantes_condicionales,RUTA_DATOS_ESTUDIANTESCOND)
    except Exception:
        print("Hubo un error")
            
def agregar_ruta(datos_estudiantes_Cursando):
    try:
        rutas=[]
        ruta= input("Ingrese la ruta que desea agregar y agrega el nombre del profesor de esta ruta, ejemplo¨: [JAVA-ARLEYM]:")
        for i in datos_estudiantes_Cursando:
            if ruta in i:
                print("esite")
            
            else:
                datos_estudiantes_Cursando[ruta]=rutas
                guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS)
        print(datos_estudiantes_Cursando)
    except Exception:
        print("hubo un error")

def usuario_pendiente(datos_estudiantes_inscritos):
    try:
        print(datos_estudiantes_inscritos)
        doc = input("Ingrese el número del documento del usuario: ")
        for i in range(len(datos_estudiantes_inscritos["users"])):
            if doc == datos_estudiantes_inscritos["users"][i]["documento"]:
                print("Usuario encontrado")
                datos_estudiantes_inscritos["users"][i]["estado"] = "si"
                print("Aceptado")
                print("Estas son las rutas disponibles")
            for o in datos_estudiantes_Cursando:
                print(f"--> {o}")
            ruta = input("Escribe alguna de estas rutas").lower()
            print("ok")
            usuario = {}            
            usuario["nombres"] = datos_estudiantes_inscritos["users"][i]["nombres"]
            usuario["documento"] = doc
            usuario["Apellidos"] = datos_estudiantes_inscritos["users"][i]["Apellidos"]
            usuario["direccion"] = datos_estudiantes_inscritos["users"][i]["direccion"]
            usuario["Edad"] = datos_estudiantes_inscritos["users"][i]["Edad"]
            usuario["Acudiente"] = datos_estudiantes_inscritos["users"][i]["Acudiente"]
            usuario["celular"] = datos_estudiantes_inscritos["users"][i]["celular"]
            usuario["telefono"] = datos_estudiantes_inscritos["users"][i]["telefono"]
            usuario["estado"] = "cursando"
            usuario["riesgo"] = datos_estudiantes_inscritos["users"][i]["riesgo"]
            usuario["nota1"] = datos_estudiantes_inscritos["users"][i]["nota1"]
            usuario["nota2"] = datos_estudiantes_inscritos["users"][i]["nota2"]
            usuario["notaf"] = datos_estudiantes_inscritos["users"][i]["notaf"]
            usuario["inicio"] = input("Ingresa el dia de inicio de este estudiante: ").lower()
            usuario["horario"] = input("Ingresa el horario que va tener este estudiante [Tarde][Mañana]: ").lower()
            usuario["finalizacion"]=input("ingresa el dia de finalizacion del estudiante: ").lower()
            usuario["Salon"]=input("Ingresa el salon donde deseas que este el estudiante: ").lower()
            usuario["estrellas"]=""
        else:
            print("usuario o ruta erronea")
            for u in datos_estudiantes_Cursando:
                if u == ruta :
                    datos_estudiantes_Cursando[ruta].append(usuario)
                    guardar_datos(datos_estudiantes_Cursando, RUTA_DATOS_ESTUDIANTESCURS)
            datos_estudiantes_inscritos["users"].pop(i)
            guardar_datos(datos_estudiantes_inscritos, RUTA_DATOS_ESTUDIANTESINSC)    
    except Exception:
        print("hubo un error")

def editar_usuarios(datos_estudiantes_Cursando):
    try:
        print(datos_estudiantes_Cursando)
        doc= input("Ingrese el numero del documento del usuario")
        ruta = input("A que ruta pertenece? ").lower()
        for i in range(len(datos_estudiantes_Cursando[ruta])):
            if doc in datos_estudiantes_Cursando[ruta][i]["documento"]:
                print("usuario encontrado")
            datos_estudiantes_Cursando[ruta][i]["nombres"]=input("Ingrese NUEVO nombre: ")
            datos_estudiantes_Cursando[ruta][i]["Apellidos"]=input("Ingrese NUEVOS apellidos: ")
            datos_estudiantes_Cursando[ruta][i]["direccion"]=input("Ingrese NUEVA DIRECCION : ")
            datos_estudiantes_Cursando[ruta][i]["Edad"]=int(input("Ingrese Nueva edad: "))
            datos_estudiantes_Cursando[ruta][i]["Acudiente"]=input("Ingrese NUEVO NOMBRE de acudiente: ")
            datos_estudiantes_Cursando[ruta][i]["celular"]=input("Ingrese NUEVO NUMERO de celular: ")
            datos_estudiantes_Cursando[ruta][i]["telefono"]=input("Ingrese NUEVO NUMERO telefono fijo: ")
            datos_estudiantes_Cursando[ruta][i]["estado"]="cursando"
            datos_estudiantes_Cursando[ruta][i]["riesgo"]= False
            datos_estudiantes_Cursando[ruta][i]["nota"]= 0
            datos_estudiantes_Cursando[ruta][i]["aprobado"]= "No definido"
            datos_estudiantes_Cursando[ruta][i]["nota1"] = 0
            datos_estudiantes_Cursando[ruta][i]["nota2"] = 0
            datos_estudiantes_Cursando[ruta][i]["notaf"] = 0
            datos_estudiantes_Cursando[ruta][i]["inicio"] =input("Ingrese NUEVA FECHA DE INICIO: ")
            datos_estudiantes_Cursando[ruta][i]["horario"] =input("Ingrese NUEVO horario: ")
            datos_estudiantes_Cursando[ruta][i]["finalizacion"] =input("Ingrese NUEVA FECHA DE FINALIZACION: ")
            
            guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS)
    except Exception:
        print("hubo un error")
        
def menu_coordinador():
    try:
        while True:
            print("----------------------------------------------------------------")
            print("Bienvenido al menu coordinador")
            print("1. Editar usuarios")
            print("2. Aceptar usuarios pendientes")
            print("3. Agregar ruta-trainer")
            print("4. Decir si aprueba o no.")
            print("----------------------------------------------------------------")
            opc = int(input("Ingrese la opciòn que deseas--> "))
            if opc == 1:
                editar_usuarios(datos_estudiantes_Cursando) 
            elif opc == 2:
                usuario_pendiente(datos_estudiantes_inscritos)
            elif opc == 3:
                agregar_ruta(datos_estudiantes_Cursando)
            elif opc == 4:
                Aprobo_o_no(datos_estudiantes_Cursando)
            elif opc == 0:
                print("saliste...")
                break
    except Exception:
        print("hubo un error")
        menu_coordinador()
