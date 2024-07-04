
from db import connection,funciones
import os
import csv
from datetime import datetime
import pyodbc

SERVER = 'DESKTOP-6NBDFVJ'
DATABASE = 'Escuela2'
TABLE = 'Horarios'
def main():
    opciones=[1,2,3,4,5]
    conexion = connection.conectar(SERVER, DATABASE)
    
    while True:
        os.system('cls')
        print('=====MANTENIMIENTO=====')
        print(f'BASE DE DATOS: {DATABASE} | TABLA: {TABLE}')
        print('1 - Agregar \n2 - Mostrar\n3 - Actuazalizar\n4 - Eliminar\n5 - Salir\n')
        r = input('Ingrese una opción: ')
        if not r.isdigit():
            print("Ingrese un valor valido")
            r=None
            input("Dale enter para continuar")
            os.system('cls')
            continue
        r=int(r)
        if r<1 or r>len(opciones):
            print("Seleccione una opcion valida")
            r=None
            input("Dale enter para continuar")
            os.system('cls')
            continue
        if r==1:
            os.system('cls')
            while True:
                try:
                    id=input("Ingrese id: ")
                    dia = input('Ingrese un dia de la semana: ')
                    horadeinicio = input('Ingrese hora de inicio (HH:MM:SS): ')
                    horafin = input('Ingrese hora de salida (HH:MM:SS): ')
                
                    claseid = input('Ingrese una id de una clase: ')
                    claseid = int(claseid)
                    
                    
                    try:
                        
                        hora_inicio_correcta = datetime.strptime(horadeinicio, '%H:%M:%S')
                        hora_fin_correcta = datetime.strptime(horafin, '%H:%M:%S')
                        hora_inicio_str = hora_inicio_correcta.strftime('%H:%M:%S')
                        hora_fin_str = hora_fin_correcta.strftime('%H:%M:%S')
                        dist = {
                            'id':id,
                            'diasemana': dia,
                            'horadeinicio': hora_inicio_str,
                            'horafin': hora_fin_str,
                            'clase': claseid
                        }

                        result = funciones.insertar(dist, conexion,id,claseid)

                        if result:
                            print('¡Registrado exitosamente! 💕💕💕')
                            input("Dale enter para continuar ")
                            break
                       

                    except ValueError:
                        print("Formato de hora incorrecto. Por favor, ingrese la hora en el formato HH:MM:SS.")
                        input("Dale enter para continuar ")
                        os.system('cls')
                except ValueError:
                    print("Ingrese una id correct")
                    input("Dale enter para continuar")
                    continue    
        if r==2:
            funciones.mostrar(conexion)
            input("Dale enter para continuar")            
        if r==3:
            os.system('cls')
            id = input('Ingrese ID del Horario ')
            resultado = funciones.actualizar(id, conexion)
            if(resultado):
             print('Horario  actualizado exitosamente! ') 
             input("Dale enter para continuar")      
        if r==4:
            os.system('cls')
            id = input('Ingrese ID del Horario: ')
            resultado = funciones.eliminar(id, conexion)
            if(resultado):
                print('Horario eliminado exitosamente! 💕💕💕')         
                input("Dale enter para continuar")
            if (resultado)==None:
                continue    
            
        if r==5:
          break
        
if __name__ == '__main__':
    main()
