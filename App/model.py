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
    """ 
    Este indice crea un map cuyos valores son el sector concatenado con el año así sector-año.
    """
    catalog["sector-año"] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   cmpfunction=compareMapYear)
    
    catalog["year_subsector"] = mp.newMap(20,
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
    add_SectorYear(data_structs , data)
    addYear2(data_structs , data)
    
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
        
def add_SectorYear(data_structs , data):
    try:
        sectoryear_map = data_structs["sector-año"] #Aqui esta el map vacio
        data_year = data["Año"].strip()
        data_sector = data["Código sector económico"].strip()
        concat = data_sector + "-" + data_year
        exist_concat = mp.contains(sectoryear_map , concat) #pregunto si contiene el mapa el concat
        
        if exist_concat:
            entry = mp.get(sectoryear_map , concat)
            entry_value = me.getValue(entry)
        else:
            entry_value = newconcat(concat)
            mp.put(sectoryear_map , concat , entry_value)
        lt.addLast(entry_value["data"] , data)
    except Exception:
        return None

def newconcat(concat):
    """
    Esta funcion crea la estructura de actividades año concatenadas
    """
    entry = {'concat': "", "data": None}
    entry['concat'] = concat
    entry['data'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry

def addYear2(data_structs , data):
    try:
        year_map = data_structs["year_subsector"] #Aqui esta el map vacio
        data_year = int(data["Año"])
        exist_year = mp.contains(year_map , data_year) #pregunto si contiene el mapa el año
        
        if exist_year:
            entry = mp.get(year_map , data_year)
            entry_value = me.getValue(entry)
        else:
            entry_value = newYear2(data_year)
            mp.put(year_map , data_year , entry_value)
        lt.addLast(entry_value["data"] , data)
        
        add_map_subsector(entry_value , data)
    except Exception:
        return None

def newYear2(year):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "data": None , "map_subsector" : None}
    entry['year'] = year
    entry['data'] = lt.newList('SINGLE_LINKED', compareYears)
    entry['map_subsector'] = mp.newMap(20,
                                   maptype='CHAINING',
                                   loadfactor=1,
                                   cmpfunction=compareMapYear)
    
    return entry

def add_map_subsector(entry_value , data):
    try:
        subsector_map = entry_value["map_subsector"] #Aqui esta el map vacio
        
        data_subsector = int(data["Código subsector económico"])
        exist_subsector = mp.contains(subsector_map , data_subsector) #pregunto si contiene el mapa el subsector
        
        if exist_subsector:
            entry = mp.get(subsector_map , data_subsector)
            entry_value_subsec = me.getValue(entry)
        else:
            entry_value_subsec = newSubsector(data_subsector)
            mp.put(subsector_map , data_subsector , entry_value_subsec)
        lt.addLast(entry_value_subsec["data"] , data)
        
    except Exception:
        return None

def newSubsector(data_subsector):
    """
    Esta funcion crea la estructura de taxes asociados
    a un subsector.
    """
    entry = {'subsector': "", "data": None}
    entry['subsector'] = data_subsector
    entry['data'] = lt.newList('SINGLE_LINKED')
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


def req_1(data_structs , concat):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    map_sec_año = data_structs["sector-año"]
    llave_valor = mp.get(map_sec_año , concat)
    valor = me.getValue(llave_valor)
    list_valor = valor["data"] #lista con las actividades del año y subsector
    s_list_valor = merg.sort(list_valor , cmp_impuestos_by_total_saldo)
    first = lt.firstElement(s_list_valor) #Mayor saldo a pagar
    return first
    
    


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs , year):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    map_year_subsector = data_structs["year_subsector"]
    key_value_year = mp.get(map_year_subsector , int(year))
    year_sub_map = me.getValue(key_value_year) #aca tengo el entry para una año específico.
    map_subsector = year_sub_map["map_subsector"] #extraigo del entry el mapa cuyas lleves son subsectores.
    
    #Ahora debo encontrar el subsector con el menor total de retenciones (Total retenciones)
    #Saco las llaves del map en una lista
    lista_keys = mp.keySet(map_subsector)
    
    position = find_subsector(lista_keys , map_subsector)
    
    #Aca lo importante es saber que subsector fue el que menos aportó
    
    elemento_ret = lt.getElement(lista_keys , position) #Este es el subsector
    
    #Extraigo ese elemento
    
    subsector_key_val = mp.get(map_subsector , elemento_ret)
    subsector_val = me.getValue(subsector_key_val)
    data_subector = subsector_val["data"] #Aca tengo una lista con las actividades.
    
    #Sacar las que mas y menos aportaron
    #1 Hacer el sort
    s_data_subector = merg.sort(data_subector , cmp_impuestos_by_total_ret)
    #Ya puedo enviar la lista ordenada al view para que tome las 3 primeras y tres ultimas
    #Solo me falta hacer la sumatoria de los datos del subector.
    #Los totales son:
    # Código sector económico. 1
    # Nombre sector económico.2
    # Código subsector económico. 3
    # Nombre subsector económico. 4
    # El total retenciones. 5
    # El total ingresos netos. 6
    # El total costos y gastos. 7
    # El total saldo por pagar. 8
    # El total saldo a favor. 9
    
    #Acá retornare una lista con la información para acomodar en el view.
    lista_ret_subsector = lt.newList()
    
    codigo_sector = None
    nombre_sector = None
    cod_sub = None
    name_sub = None
    total_retenciones = 0
    total_ingresos = 0
    total_costos_gas = 0
    total_saldo_pagar = 0
    total_saldo_favor = 0
    
    #Tomo un elemento cualquiera
    elemento_cualquiera = lt.getElement(s_data_subector , 1)
    codigo_sector = elemento_cualquiera["Código sector económico"]
    nombre_sector = elemento_cualquiera["Nombre sector económico"]
    cod_sub = elemento_cualquiera["Código subsector económico"]
    name_sub = elemento_cualquiera["Nombre subsector económico"]
    
    
    
    
    for element in lt.iterator(s_data_subector):
        total_retenciones += int(element["Total retenciones"])
        total_ingresos += int(element["Total ingresos netos"])
        total_costos_gas += int(element["Total costos y gastos"])
        total_saldo_pagar += int(element["Total saldo a pagar"])
        total_saldo_favor += int(element["Total saldo a favor"])
    
    lt.addLast(lista_ret_subsector , codigo_sector)
    lt.addLast(lista_ret_subsector , nombre_sector)
    lt.addLast(lista_ret_subsector , cod_sub)
    lt.addLast(lista_ret_subsector , name_sub)
    lt.addLast(lista_ret_subsector , total_retenciones)
    lt.addLast(lista_ret_subsector , total_ingresos)    
    lt.addLast(lista_ret_subsector , total_costos_gas)
    lt.addLast(lista_ret_subsector , total_saldo_pagar)
    lt.addLast(lista_ret_subsector , total_saldo_favor)
    
    return lista_ret_subsector , s_data_subector
    #Finalmente se retorna una lista con los elementos del subsector para el primer print
    # y la lista de actividades para sacar las primeras tres y las ultimas tres.
    
def find_subsector(lista_keys , map_subsector):
    """
    Esta funcion debe hallar el subsector con menor total de retenciones (Total retenciones)
    """
    total_retenciones = None
    pos = 1
    pos_in = 1
    for element in lt.iterator(lista_keys):
        key_value = mp.get(map_subsector , element) #Extraigo los subsectores 1 a 1
        value = me.getValue(key_value) #Tengo aca la estructura {subector : "" , data: "" , data tiene la lista}
        data_acitividades = value["data"] #Esto es una list
        
        #Ahora lo que sigue es iterar sobre cada actividad y sumar las retenciones.
        tot_parcial_ret = 0
        for element in lt.iterator(data_acitividades):
            retenciones = int(element["Total retenciones"]) #Extraigo las retenciones del elemento
            tot_parcial_ret += retenciones
        
        #Con el total de retenciones completos ahora comparamos con total_retenciones.
        
        if total_retenciones == None: #Primera iteración
            total_retenciones = tot_parcial_ret
        elif tot_parcial_ret < total_retenciones: #si el total parcial es menor al anterior reemplazar
            total_retenciones = tot_parcial_ret
            pos = pos_in
        pos_in += 1
    
    return pos
        
        
    


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


def req_7(data_structs , año , cod_sub):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    map_year = data_structs["year_subsector"]
    key_val = mp.get(map_year , año)
    val = me.getValue(key_val)
    sublist_map = val["map_subsector"]
    key_val2 = mp.get(sublist_map , cod_sub)
    val2 = me.getValue(key_val2)
    lista_elementos = val2["data"] #lista con elementos
    
    ordenada = merg.sort(lista_elementos , cmp_impuestos_by_total_costos)
    return ordenada

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
    
def compareMapYear(conc , entry):
    """
    Compara dos llaves codigo-año. El primero es un str
    y el segundo un entry de un map.
    """
    entry = me.getKey(entry)
    if (conc == entry):
        return 0
    elif (conc > entry):
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
    try:
        ret_var = None
        if int(actividad1["Código actividad económica"]) < int(actividad2["Código actividad económica"]):
            ret_var = True
        else:      
            ret_var = False
        return ret_var
    
    except Exception:
        ret_var = None
        var1 = actividad1["Código actividad económica"]
        var1 = var1[0:3]
        var2 = actividad2["Código actividad económica"]
        var2 = var1[0:3]
        if int(var1) < int(var2):
            ret_var = True
        else:      
            ret_var = False
        return ret_var

def cmp_impuestos_by_total_saldo(impuesto1, impuesto2):
    ret_var = None
    if int(impuesto1["Total saldo a pagar"]) > int(impuesto2["Total saldo a pagar"]):
        ret_var = True
    else:      
        ret_var = False
        
    return ret_var

def cmp_impuestos_by_total_ret(impuesto1, impuesto2):
    ret_var = None
    if int(impuesto1["Total retenciones"]) > int(impuesto2["Total retenciones"]):
        ret_var = True
    else:      
        ret_var = False
        
    return ret_var

def cmp_impuestos_by_total_costos(impuesto1, impuesto2):
    ret_var = None
    if int(impuesto1["Total costos y gastos"]) < int(impuesto2["Total costos y gastos"]):
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
        