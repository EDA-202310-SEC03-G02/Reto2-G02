"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

default_limit = 1000 
sys.setrecursionlimit(default_limit*10) 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")
    
def print_menu_file_size():
    print("Escoja el tamaño de archivo que desea utilizar:")
    print("1- small")
    print("2- 5%")
    print("3- 10%")
    print("4- 20%")
    print("5- 30%")
    print("6- 50%")
    print("7- 80%")
    print("8- large")


def load_data(control , filesize):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data = controller.load_data(control , filesize)
    return data

def sort_year_lists(control):
    controller.sort_year_lists(control)
    
def print_carga_datos(data_size , control):
    print('Lineas cargadas: ' + str(data_size))
    controller.print_carga(control)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control , concat):
    
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    first = controller.req_1(control , concat)
    print(first["Código actividad económica"])
    dic_aux1 = {        "Código actividad económica":[first["Código actividad económica"]],
                        "Nombre actividad económica":[first["Nombre actividad económica"]],
                        "Código subsector económico":[first["Código subsector económico"]],
                        "Nombre subsector económico":[first["Nombre subsector económico"]],
                        "Total ingresos netos":[first["Total ingresos netos"]],
                        "Total costos y gastos":[first["Total costos y gastos"]],
                        "Total saldo a pagar":[first["Total saldo a pagar"]],
                        "Total saldo a favor":[first["Total saldo a favor"]]
                        }
    
    print(tabulate(dic_aux1, headers="keys", tablefmt="fancy_grid" , maxcolwidths=8 , maxheadercolwidths=6))

def print_req_2(control , año):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control , año):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    lista_ret_subsector , s_data_subector = controller.req_3(control , año)
    
    dic_aux1 = {        "Código sector económico":[lt.getElement(lista_ret_subsector , 1)],
                        "Nombre sector económico":[lt.getElement(lista_ret_subsector , 2)],
                        "Código subsector económico":[lt.getElement(lista_ret_subsector , 3)],
                        "Nombre subsector económico":[lt.getElement(lista_ret_subsector , 4)],
                        "Total retenciones":[lt.getElement(lista_ret_subsector , 5)],
                        "Total ingresos netos":[lt.getElement(lista_ret_subsector , 6)],
                        "Total costos y gastos":[lt.getElement(lista_ret_subsector ,7)],
                        "Total saldo por pagar":[lt.getElement(lista_ret_subsector , 8)],
                        "Total saldo a favor":[lt.getElement(lista_ret_subsector , 9)]
                        }
    
    print(tabulate(dic_aux1, headers="keys", tablefmt="fancy_grid" , maxcolwidths=8 , maxheadercolwidths=6))
    print("------------Contribuciones de las actividades económicas:----------")
    len = int(lt.size(s_data_subector))
    if len < 6:
        print("Solo habían " + str(len) + " actividades económicas")
        dic_aux2 = {    "Código actividad económica":[],
                        "Nombre actividad económica":[],
                        "Total retenciones":[],
                        "Total ingresos netos":[],
                        "Total costos y gastos":[],
                        "Total saldo por pagar":[],
                        "Total saldo a favor":[]
                        }
        for element in lt.iterator(s_data_subector):
            dic_aux2["Código actividad económica"].append(element["Código actividad económica"])
            dic_aux2["Nombre actividad económica"].append(element["Nombre actividad económica"])
            dic_aux2["Total retenciones"].append(element["Total retenciones"])
            dic_aux2["Total ingresos netos"].append(element["Total ingresos netos"])
            dic_aux2["Total costos y gastos"].append(element["Total costos y gastos"])
            dic_aux2["Total saldo por pagar"].append(element["Total saldo a pagar"])
            dic_aux2["Total saldo a favor"].append(element["Total saldo a favor"])
        

        print(tabulate(dic_aux2, headers="keys", tablefmt="fancy_grid" , maxcolwidths=8 , maxheadercolwidths=6))
        
    else:
        print("Las tres actividades que menos aportaron fueron: ")
        dic_aux3 = {    "Código actividad económica":[],
                        "Nombre actividad económica":[],
                        "Total retenciones":[],
                        "Total ingresos netos":[],
                        "Total costos y gastos":[],
                        "Total saldo por pagar":[],
                        "Total saldo a favor":[]}
        
        sublist1 = lt.subList(s_data_subector , 1 , 3)
        for element in lt.iterator(sublist1):
            dic_aux2["Código actividad económica"].append(element["Código actividad económica"])
            dic_aux2["Nombre actividad económica"].append(element["Nombre actividad económica"])
            dic_aux2["Total retenciones"].append(element["Total retenciones"])
            dic_aux2["Total ingresos netos"].append(element["Total ingresos netos"])
            dic_aux2["Total costos y gastos"].append(element["Total costos y gastos"])
            dic_aux2["Total saldo por pagar"].append(element["Total saldo a pagar"])
            dic_aux2["Total saldo a favor"].append(element["Total saldo a favor"])
        
        
        print(tabulate(dic_aux3, headers="keys", tablefmt="fancy_grid" , maxcolwidths=8 , maxheadercolwidths=6))
            
        print("Las tres actividades que más aportaron fueron: ")
        
        dic_aux4 = {    "Código actividad económica":[],
                        "Nombre actividad económica":[],
                        "Total retenciones":[],
                        "Total ingresos netos":[],
                        "Total costos y gastos":[],
                        "Total saldo por pagar":[],
                        "Total saldo a favor":[]}
        sublist2 = lt.subList(s_data_subector , len-2 , 3)
        for element in lt.iterator(sublist2):
            dic_aux2["Código actividad económica"].append(element["Código actividad económica"])
            dic_aux2["Nombre actividad económica"].append(element["Nombre actividad económica"])
            dic_aux2["Total retenciones"].append(element["Total retenciones"])
            dic_aux2["Total ingresos netos"].append(element["Total ingresos netos"])
            dic_aux2["Total costos y gastos"].append(element["Total costos y gastos"])
            dic_aux2["Total saldo por pagar"].append(element["Total saldo a pagar"])
            dic_aux2["Total saldo a favor"].append(element["Total saldo a favor"])
        
        print(tabulate(dic_aux4, headers="keys", tablefmt="fancy_grid" , maxcolwidths=8 , maxheadercolwidths=6))
        
        
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
#control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                control = new_controller()
                print_menu_file_size()
                filesize = input("Seleccione una opción: \n")
                data_size = load_data(control , filesize) #Se cargan datos y se guarda el tamaño en data_size
                sort_year_lists(control) 
                print_carga_datos(data_size , control)
                
                
            
            elif int(inputs) == 2:
                sector_economico = input("Ingrese el sector económico que desea consultar: ").strip()
                año_buscar = input("Ingrese el año que desea consultar: ").strip()
                concat = sector_economico + "-" + año_buscar
                print_req_1(control , concat)

            elif int(inputs) == 3:

                print_req_2(control)

            elif int(inputs) == 4:
                año = int(input("Ingrese el año que desea consultar: "))
                print_req_3(control , año)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
