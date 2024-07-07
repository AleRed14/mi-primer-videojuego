def obtener_path_actual(nombre_archivo:str):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def new_puntaje(nombre:str, score:int)->dict:
    puntaje = {}
    puntaje["nombre"] = nombre
    puntaje["score"] = score
    return puntaje

def cargar_lista_csv(nombre_archivo:str)->list:
    """Carga los datos de un archivo csv a una lista

    Args:
        nombre_archivo (str): nombre del archivo que buscamos

    Returns:
        list: Lista con diccionarios de los datos del archivo
    """
    lista = []
    with open(obtener_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip("\n").split(",")
        # El slip separa un string por el parametro que le pasemos (en este caso
        # una coma) y lo mete en una lista
        # print(encabezado)
        for linea in archivo.readlines():
            linea = linea.strip("\n").split(",")
            # linea se convierte en una lista donde los datos son sus elementos.
            # print(linea)
            nombre, score = linea 
            # se llama umpacking o desempacar
            # a cada uno de esos elementos se le asigna una variable.
            # print(linea)
            lista.append(new_puntaje(nombre, int(score)))
            # Se agregan los elementos a un diccionarios que se agrega a una lista.
            # print(dato)
        # print(linea)
    # for persona in lista:
    #     print(persona)
    # print(lista)
    return lista

def crear_archivo_csv(nombre_archivo:str, lista:list)->None:
    with open(obtener_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            lista_values = []
            for value in values:
                
                if isinstance(value,int):
                    lista_values.append(str(value))
                elif isinstance(value,float):
                    lista_values.append(str(value))
                else:
                    lista_values.append(value)
            linea = ",".join(lista_values) + "\n"
            archivo.write(linea)
def append_archivo_csv(nombre_archivo:str, lista:list)->None:
    with open(obtener_path_actual(nombre_archivo), "a", encoding="utf-8") as archivo:
        # encabezado = ",".join(list(lista[0].keys())) + "\n"
        # archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            lista_values = []
            for value in values:
                
                if isinstance(value,int):
                    lista_values.append(str(value))
                elif isinstance(value,float):
                    lista_values.append(str(value))
                else:
                    lista_values.append(value)
            linea = ",".join(lista_values) + "\n"
            archivo.write(linea)

def cargar_lista_json(nombre_archivo:str)->list:
    import json
    with open(obtener_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        personas = json.load(archivo)
    return personas

def crear_archivo_json(nombre_archivo:str, lista:list)->None:
    import json
    with open(obtener_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)

def append_archivo_json(nombre_archivo:str, lista:list)->None:
    import json
    with open(obtener_path_actual(nombre_archivo), "a", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)