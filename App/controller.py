"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
import tracemalloc
csv.field_size_limit(2147483647) 

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos

def load_data(control, filesize):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    data_structs = control['model']
    str_conc = filesize_converter(filesize) #Pedazo de string que concatenaremos
    datafile = cf.data_dir + 'DIAN/Salida_agregados_renta_juridicos_AG' + str_conc + ".csv"
    input_file = csv.DictReader(open(datafile, encoding='utf-8'))
    for data in input_file:
        model.add_data(data_structs, data)
    return model.data_size(data_structs)

def filesize_converter(filesize):
    """
    Esta funcion convierte el valor enviado desde el menú a un string para introducir
    en la ruta del archivo
    """
    return_var = None
    if int(filesize) == 1:
        return_var = "-small"
    if int(filesize) == 2:
        return_var = "-5pct"
    if int(filesize) == 3:
        return_var = "-10pct"
    if int(filesize) == 4:
        return_var = "-20pct"
    if int(filesize) == 5:
        return_var = "-30pct"
    if int(filesize) == 6:
        return_var = "-50pct"
    if int(filesize) == 7:
        return_var = "-80pct"
    if int(filesize) == 8:
        return_var = "-large"
    
    return return_var

def print_carga(control):
    data_structs = control["model"]
    model.print_carga_datos(data_structs)

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass

def sort_year_lists(control):
    data_structs = control["model"]
    model.sort_year_lists(data_structs)


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control , concat):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    t1 = get_time()
    data_structs = control["model"]
    first = model.req_1(data_structs, concat)
    t2 = get_time()
    delta_time = t2 - t1
    return first , delta_time


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control , año):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    t1 = get_time()
    data_structs = control["model"]
    lista_ret_subsector , s_data_subector = model.req_3(data_structs , año)
    t2 = get_time()
    delta_time = t2 - t1
    return lista_ret_subsector , s_data_subector , delta_time


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control , año , cod_sub):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    data_structs = control["model"]
    ordenada = model.req_7(data_structs , año , cod_sub)
    return ordenada

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
