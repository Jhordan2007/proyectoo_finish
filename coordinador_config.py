import json #IMPORTAMOS O TRAEMOS PARA PODER TOMAR LOS JSON QUE NECESITEMOS
from datos import * #Importamos los datos de cargar_datos y guardar_datos
from registrar_camper import* #importamos el registrar_camper que es donde esta las funciones para reigstrar al camper 
RUTA_DATOS_ESTUDIANTESEXP = "estudiantes_expulsados.json" #llamamos al json, este json es el de expulsados y lo guardamos en una variable 
datos_estudiantes_expulsados = cargar_datos(RUTA_DATOS_ESTUDIANTESEXP) #guardamos la variable que vamos a usar para guardar y dentro del "cargar_datos" encontramos donde guardamos al json

RUTA_DATOS_ESTUDIANTESCOND = "estudiantes_condicionales.json"
datos_estudiantes_condicionales = cargar_datos(RUTA_DATOS_ESTUDIANTESCOND)


RUTA_DATOS_ESTUDIANTESCURS = "estudiantes_Cursando.json"
datos_estudiantes_Cursando = cargar_datos(RUTA_DATOS_ESTUDIANTESCURS)

RUTA_DATOS_ESTUDIANTESINSC = "estudiantes_inscritos.json"
datos_estudiantes_inscritos = cargar_datos(RUTA_DATOS_ESTUDIANTESINSC)


#función para el coordinador apruebe estudiantes, desea expulsarlo, dejarlo condicional o dejarlo cursando
def Aprobo_o_no(datos_estudiantes_Cursando):
    try:
        doc= input("Ingrese el numero del documento del usuario") #ingresamos el numero de documento del estudiante que queremos ver si aprobar o no o si queremos colocr en condicional
        for o in datos_estudiantes_Cursando: #recorremos lo que hay en el json datos_estudiantes_cursando
            print(f"-->{o}") #escribimos lo que hay en ese json como llaves iniciales que en mi caso son la ruta con su profesor 
        ruta = input("A que ruta pertenece?").lower() #aca pedimos la ruta y la almacenamos en una variable, el .lower es para colocar todos los caracteres a minusculas 
        for u in range(len(datos_estudiantes_Cursando[ruta])): #Recorremos lo que hay dentro de esa ruta y se almacena en la u 
            print("la nota definitiva de estudiante es: ",datos_estudiantes_Cursando[ruta][u]["notaf"]) #nos muestra la nota final del estudainte para que el coordinador decida que hacer  
            if doc  == datos_estudiantes_Cursando[ruta][u]["documento"]: #valida que sea el estudiante con el documento ingresado
                print("usuario encontrado") #nos valida que si encontro el estudiante 
                test = input("Desea aprobarlo, condicional, no aprobarlo? [Si][Condicional][No]").lower() #almacenamos en una variable la respuesta del coordinador
                if test == "no": #validamos cual es la respuesta para ver que se desea hacer con el estudiante
                    for i in range(len(datos_estudiantes_Cursando[ruta])):  #recorremos lo que hay dentro de esa ruta y lo almacena en la i 
                        if datos_estudiantes_Cursando[ruta][i]["documento"]== doc: #hacemos otro for de validacion para el documento
                            usuario = {} #Creamos un dicconario donde vamos almacenar los valores de ese estudiante que deseamos expulsar             
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
                            datos_estudiantes_expulsados["expulsados"].append(usuario) #agregamos el estudiante al json de expulsados junto a todos sus datos 
                            datos_estudiantes_Cursando[ruta].pop(i) #elimianos el estudiante del json donde estaba 
                if test == "condicional": #validamos la opcion que se ejecuto
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
                            datos_estudiantes_condicionales["condicionales"].append(usuario) #agregamos el estudiante al nuevo json
                            datos_estudiantes_Cursando[ruta].pop(i) #eliminamos el estudiante del anterior json 
                guardar_datos(datos_estudiantes_Cursando, RUTA_DATOS_ESTUDIANTESCURS) #guardamos los datos del estudiante cursando en la ruta de espulsados 
                guardar_datos(datos_estudiantes_expulsados, RUTA_DATOS_ESTUDIANTESEXP) #guardamos por completo los estudiantes de expulsados 
                guardar_datos(datos_estudiantes_condicionales,RUTA_DATOS_ESTUDIANTESCOND) #guardamos el nuevo estudiante condicional 
    except Exception:
        print("Hubo un error")
#AGREGAR UNA NUEVA RUTA JUNTO A SU TRAINER
def agregar_ruta(datos_estudiantes_Cursando):
    try:
        rutas=[] #Almacenamos rutas en lista por lo que las rutas son listas que contienen diccionarios 
        ruta= input("Ingrese la ruta que desea agregar y agrega el nombre del profesor de esta ruta, ejemplo¨: [JAVA-ARLEYM]:") #Decidimos la nueva ruta que vamos agregar, esa ruta tiene que traer su trainer 
        for i in datos_estudiantes_Cursando: #recorremos lo que hay en estudiantes cursando y se almacena en la variable i 
            if ruta in i: #validamos si hay una ruta con el mismo nombre o no
                print("esite") #nos confirma que esa ruta ya existe
            # decide que si no existe ya esa ruta la crea 
            else:
                datos_estudiantes_Cursando[ruta]=rutas #agregamos la nueva ruta a que se vuelva lista
                guardar_datos(datos_estudiantes_Cursando,RUTA_DATOS_ESTUDIANTESCURS) # guardamos la nueva la ruta que creamos
        print(datos_estudiantes_Cursando) 
    except Exception:
        print("hubo un error")
#ESTA FUNCION NOS PERMITE ACEPTAR A UN USUARIO QUE SE ENCUENTRA EN INSCRITO PARA VER SI LO PODEMOS PASAR A USUARIO CURSANDO
def usuario_pendiente(datos_estudiantes_inscritos):
    try:
        print(datos_estudiantes_inscritos) 
        doc = input("Ingrese el número del documento del usuario: ") #Pedimos documento y lo almacenamos en una variable
        for i in range(len(datos_estudiantes_inscritos["users"])): #Recorremos lo que hay en usuarios 
            if doc == datos_estudiantes_inscritos["users"][i]["documento"]: #Validamos que exista ese usuario 
                print("Usuario encontrado")
                datos_estudiantes_inscritos["users"][i]["estado"] = "si" #decidimos pasar su estado a si o sea aprobado 
                print("Aceptado") 
                print("Estas son las rutas disponibles") 
            for o in datos_estudiantes_Cursando: #recorremos las rutas que tenemos en estudiantes_cursando
                print(f"--> {o}") #nos imprime las rutas que se almacenaron en o
            ruta = input("Escribe alguna de estas rutas").lower() # pedimos la ruta a la cual queremos agregar 
            print("ok")
            usuario = {} #creamos un diccionario donde vamos almacenar los datos de nuestro estudiante inscrito 
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
            usuario["inicio"] = input("Ingresa el dia de inicio de este estudiante: ").lower() #nos pide un dato nuevo que es el dia de inicio de este camper 
            usuario["horario"] = input("Ingresa el horario que va tener este estudiante [Tarde][Mañana]: ").lower() #nos pide el horario donde se manejar este camper
            usuario["finalizacion"]=input("ingresa el dia de finalizacion del estudiante: ").lower() #nos pide un dato nuevo que es el dia de inicio de este camper 
            usuario["Salon"]=input("Ingresa el salon donde deseas que este el estudiante: ").lower() #nos pide un dato nuevo que es el salon donde desea dejarlo
            usuario["estrellas"]="" #funcion especial
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
