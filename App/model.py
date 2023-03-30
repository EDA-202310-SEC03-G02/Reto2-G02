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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from tabulate import tabulate
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {"data":None,
                    "year":None
                    }
    
    catalog["data"] = lt.newList("SINGLE_LINKED" , compare)
    
    """ 
    Este indice crea un map cuyos valores son los años de las actividades.
    """
    catalog["year"] = mp.newMap(20,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   cmpfunction=compareMapYear)
    
    return catalog
    

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs['data'], data)
    addYear(data_structs , data)
    
def addYear(data_structs , data):
    try:
        year_map = data_structs["year"] #Aqui esta el map vacio
        data_year = int(data["Año"])
        exist_year = mp.contains(year_map , data_year) #pregunto si contiene el mapa el año
        
        if exist_year:
            entry = mp.get(year_map , data_year)
            entry_value = me.getValue(entry)
        else:
            entry_value = newYear(data_year)
            mp.put(year_map , data_year , entry_value)
        lt.addLast(entry_value["data"] , data)
    except Exception:
        return None
            
def newYear(year):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "data": None}
    entry['year'] = year
    entry['data'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry
        


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    
    if data_1 == data_2:
        return 0
    elif data_1 > data_2:
        return 1
    else:
        return -1
    
def compareMapYear(year , entry):
    """
    Compara dos años. El primero es un int
    y el segundo un entry de un map.
    """
    yearentry = me.getKey(entry)
    if (year == yearentry):
        return 0
    elif (year > yearentry):
        return 1
    else:
        return -1
    
def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return -1
    
def compareYears2(year1, year2):
    ret_var = None
    if int(year1) < (year2):
        ret_var = True
    else:      
        ret_var = False
        
    return ret_var

def cmp_codigo_act_ec(actividad1, actividad2):
    ret_var = None
    if int(actividad1["Código actividad económica"]) < int(actividad2["Código actividad económica"]):
        ret_var = True
    else:      
        ret_var = False
        
    return ret_var

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def sort_year_lists(data_structs):
    year_map = data_structs["year"]
    keys = mp.keySet(year_map) #Saco las llaves en una lista disclib
    for key in lt.iterator(keys):
        key_value = mp.get(year_map , key)
        value = me.getValue(key_value)
        list_to_sort = value["data"]
        sort_list_by_code(list_to_sort)
        
def sort_list_by_code(list_to_sort):
    merg.sort(list_to_sort , cmp_codigo_act_ec)    


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

#Funciones para acomodar los datos a imprimir

def print_carga_datos(data_structs):
    map_year = data_structs["year"]
    keys_years = mp.keySet(map_year) #Saca las llaves a lt.list
    s_keys_years = merg.sort(keys_years , compareYears2)
    for element in lt.iterator(s_keys_years):
        print(element , "Holallalalal")
    
    for key in lt.iterator(s_keys_years): #loop para tomar cada año
        key_value = mp.get(map_year , key)
        value = me.getValue(key_value)
        data_list = value["data"] #lista con act_econ del año ordenadas por codigo
        len_data_list = int(lt.size(data_list))
        
        dic_aux1 = {"Año":[],
                        "Código actividad económica":[],
                        "Nombre actividad económica":[],
                        "Código sector económico":[],
                        "Nombre sector económico":[],
                        "Código subsector económico":[],
                        "Nombre subsector económico":[],
                        "Total ingresos netos":[],
                        "Total costos y gastos":[],
                        "Total saldo a pagar":[],
                        "Total saldo a favor":[]
                        }
        
        if len_data_list < 6:
            print("Hay solo " + str(len_data_list) + " actividades económicas en el año " + str(key))
            
            for element in lt.iterator(data_list):
                dic_aux1["Año"].append(element["Año"])
                dic_aux1["Código actividad económica"].append(element["Código actividad económica"])
                dic_aux1["Nombre actividad económica"].append(element["Nombre actividad económica"])      
                dic_aux1["Código sector económico"].append(element["Código sector económico"])
                dic_aux1["Nombre sector económico"].append(element["Nombre sector económico"])
                dic_aux1["Código subsector económico"].append(element["Código subsector económico"])
                dic_aux1["Nombre subsector económico"].append(element["Nombre subsector económico"])
                dic_aux1["Total ingresos netos"].append(element["Total ingresos netos"])
                dic_aux1["Total costos y gastos"].append(element["Total costos y gastos"])
                dic_aux1["Total saldo a pagar"].append(element["Total saldo a pagar"])
                dic_aux1["Total saldo a favor"].append(element["Total saldo a favor"])
                
        else:
            print("Los primeros tres y últimos tres elementos del año" + str(key) + " son: ")
            sublist1 = lt.subList(data_list , 1 , 3)
            sublist2 = lt.subList(data_list , len_data_list-2 , 3)
            for element in lt.iterator(sublist1):
                dic_aux1["Año"].append(element["Año"])
                dic_aux1["Código actividad económica"].append(element["Código actividad económica"])
                dic_aux1["Nombre actividad económica"].append(element["Nombre actividad económica"])      
                dic_aux1["Código sector económico"].append(element["Código sector económico"])
                dic_aux1["Nombre sector económico"].append(element["Nombre sector económico"])
                dic_aux1["Código subsector económico"].append(element["Código subsector económico"])
                dic_aux1["Nombre subsector económico"].append(element["Nombre subsector económico"])
                dic_aux1["Total ingresos netos"].append(element["Total ingresos netos"])
                dic_aux1["Total costos y gastos"].append(element["Total costos y gastos"])
                dic_aux1["Total saldo a pagar"].append(element["Total saldo a pagar"])
                dic_aux1["Total saldo a favor"].append(element["Total saldo a favor"])
            
            for element in lt.iterator(sublist2):
                dic_aux1["Año"].append(element["Año"])
                dic_aux1["Código actividad económica"].append(element["Código actividad económica"])
                dic_aux1["Nombre actividad económica"].append(element["Nombre actividad económica"])      
                dic_aux1["Código sector económico"].append(element["Código sector económico"])
                dic_aux1["Nombre sector económico"].append(element["Nombre sector económico"])
                dic_aux1["Código subsector económico"].append(element["Código subsector económico"])
                dic_aux1["Nombre subsector económico"].append(element["Nombre subsector económico"])
                dic_aux1["Total ingresos netos"].append(element["Total ingresos netos"])
                dic_aux1["Total costos y gastos"].append(element["Total costos y gastos"])
                dic_aux1["Total saldo a pagar"].append(element["Total saldo a pagar"])
                dic_aux1["Total saldo a favor"].append(element["Total saldo a favor"])
        
        print(tabulate(dic_aux1, headers="keys", tablefmt="fancy_grid" , maxcolwidths=8 , maxheadercolwidths=6))