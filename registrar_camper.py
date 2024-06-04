import json
from datos import *
def registrar_usuario(datos_estudiantes_inscritos):
    try:
        Usuario={}
        doc= int(input("Ingrese su numero de documento"))
        if doc in datos_estudiantes_inscritos["users"]:
            print("esite")            
        else: 
            Usuario={}
            Usuario["nombres"] = input("ingrese sus nombre: ")
            Usuario["documento"] = doc
            Usuario["Apellidos"] = input("ingrese sus apellidos: ")
            Usuario["direccion"] = input("ingrese su direccion: ")
            Usuario["Edad"] = input("ingrese su edad: ")
            Usuario["Acudiente"] = input("ingrese su acudiente: ")
            Usuario["celular"] = input("ingrese su celular: ")
            Usuario["telefono"] = input("ingrese su telefono: ")
            Usuario["estado"] = "no"
            Usuario["riesgo"] = False
            Usuario["aprobo"] = ""
            Usuario["nota1"] = 0
            Usuario["nota2"] = 0
            Usuario["notaf"] = 0

            datos_estudiantes_inscritos["users"].append(Usuario)
            return datos_estudiantes_inscritos
        print("guardado con exito")

        print(datos_estudiantes_inscritos)
    except Exception:
        print("hubo un error")
    
    #medio