import pyodbc
import os
from datetime import datetime
def insertar(dist, conexion,id,claseid):
    try:
        cursor = conexion.cursor()
        sql="SELECT COUNT(*) FROM Horarios WHERE HorarioID=?"
        veri=(id)
        cursor.execute(sql,veri)
        validar=cursor.fetchone()[0]
        if validar>0:
            print(f'Error:el id que ingresaste:{id}  ya existe ')
            input("dale enter para continuar")
            os.system('cls')
            return
        sql2="SELECT COUNT(*) FROM Clases WHERE ClaseID=?"
        veri2=(claseid)
        cursor.execute(sql2,veri2)
        validar2=cursor.fetchone()[0]
        if validar2==0:
            print(f'Error : el id :{claseid} que ingresate no se encuentra ')
            input("dale enter para continuar")
            os.system('cls')
            return
            
        query = 'INSERT INTO Horarios VALUES(?,?, ?, ?,?)'
        cursor.execute(query,dist['id'], dist['diasemana'], dist['horadeinicio'], dist['horafin'],dist['clase'])
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al insertar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
def buscar(id, conexion):
    try:
        cursor = conexion.cursor()
        query = 'SELECT * FROM Horarios WHERE HorarioID = ?'
        cursor.execute(query, id)
        resultado = cursor.fetchone()
        return resultado
    except pyodbc.Error as error:
        print(f'Error al buscar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def actualizar(id, conexion):
    opciones=[1,2,3,4,5]
    try:
        while True:
            os.system('cls')
            resultado = buscar(id, conexion)
            if not resultado:
                print('Horario  no encontrado...')
                input('Presione Enter para continuar...')
                return None
            print('===Horarios===')
            print(f"ID: {id}\nDia de la semana: {resultado[1]}\nHora de Inicio: {resultado[2]}\nHora Final: {resultado[3]}\nClase ID : {resultado[4]}")
            print('Escoja campo a actualizar:\n1 - Dia de la semana\n2 - Hora de Inicio\n3 - Hora Final\n4 - Todos los campos\n5 - Cancelar')
            r = (input())
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
            cursor = conexion.cursor()
            match r:
                case 1:
                    diasemana =input('Ingrese nuevo dia de semana: ')
                    query = 'UPDATE Horarios SET DiaSemana = ? WHERE HorarioID = ?'
                    cursor.execute(query, diasemana, id)
                case 2:
                    while True:
                        try:
                            horainicio = input('Ingrese la nueva hora de inicio (HH:MM:SS): ')
                            hora_inicio_correcta = datetime.strptime(horainicio, '%H:%M:%S')
                            hora_inicio_str = hora_inicio_correcta.strftime('%H:%M:%S')
                            query = 'UPDATE Horarios SET HoraInicio = ? WHERE HorarioID = ?'
                            cursor.execute(query, hora_inicio_str, id)
                            break
                        except ValueError:
                            print("Formato de hora incorrecto. Por favor, ingrese la hora en el formato HH:MM:SS.")
                            input("Dale enter para continuar ")
                            os.system('cls')    
                case 3:
                    try:
                        Horafinal = input('Ingrese nueva hora final (HH:MM:SS): ')
                        hora_fin_correcta = datetime.strptime(Horafinal, '%H:%M:%S')
                        hora_fin_str = hora_fin_correcta.strftime('%H:%M:%S')
                        query = 'UPDATE Horarios SET HoraFin = ? WHERE HorarioID = ?'
                        cursor.execute(query, hora_fin_str, id)
                    except ValueError:
                            print("Formato de hora incorrecto. Por favor, ingrese la hora en el formato HH:MM:SS.")
                            input("Dale enter para continuar ")
                            os.system('cls')    
                case 4: 
                    diasemana = input('Ingrese nuevo Dia de la semana: ')
                    horainicio = input('Ingrese nueva hora de inicio (HH:MM:SS): ')
                    Horafinal= input('Ingrese nueva hora final (HH:MM:SS): ')
                    query = 'UPDATE Horarios SET DiaSemana = ?, HoraInicio = ?, HoraFin = ? WHERE HorarioID = ?'
                    cursor.execute(query, diasemana,horainicio,Horafinal, id)
                case 5:
                    return
            cursor.commit()
            cursor.close()
            return True
    except pyodbc.Error as error:
        print(f'Error al actualizar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None    
    
def mostrar(conexion):
    try:
        os.system('cls')
        cursor=conexion.cursor()
        cursor.execute('select * from Horarios')
        data=cursor.fetchall()
        encabezados=["Horario ID","Dia Semana","Hora Inicio","Hora Fin","CLASE ID"]
        lista_final=[encabezados]+[list(fila)for fila in data]
        anchos_columnas=[max(len(str(item))for item in col)for col in zip(*lista_final)]
        for fila in lista_final:
            print("|".join(f'{str(item):<{anchos_columnas[i]}}'for i,item in enumerate (fila)))
        
    except pyodbc.Error as error:
        print(f'Error al buscar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
def eliminar(id,conexion):
    while True:
        try:
            resultado = buscar(id, conexion)
            if not resultado:
                print('Distribuidor no encontrado...')
                input('Presione Enter para continuar...')
                return None
            print('===Horarios===')
            print(f"ID: {id}\nDia de la semana: {resultado[1]}\nHora de Inicio: {resultado[2]}\nHora Final: {resultado[3]}\nClase ID : {resultado[4]}")
            print('Desea eliminarlo?:\n1 - Si\n2 - No')
            r = int(input())
            match r:
                case 1:
                    cursor = conexion.cursor()
                    cursor.execute('DELETE FROM Horarios WHERE HorarioID = ?', id)
                    cursor.commit()
                    cursor.close()
                    return True
                case 2:
                    return False
            
        except pyodbc.Error as error:
            print(f'Error al actualizar 💀💀💀. Error: {error}')
            cursor.close()
            input('Presione Enter para continuar...')
            return None    