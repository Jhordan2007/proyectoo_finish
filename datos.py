import json

def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        Data = json.load(file)
    return Data
    
def guardar_datos(datos, archivo):
    datos = dict(datos)
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")  
    file.write(diccionario)
    file.close()
    #medio