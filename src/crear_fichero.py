import os

nombre_archivo = "./src/datos-peso-corporal.txt"
datos_guardados = []

def cargar_desde_txt():
    
    datos = []
    if not os.path.exists(nombre_archivo):
        return datos

    try:
        with open(nombre_archivo, 'r') as archivo:
            archivo.readline() 
            
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                
                try:
                    partes = linea.split(',')
                    nombre = partes[0].strip()
                    peso_str = partes[1].strip().replace(" Kg", "") 
                    peso = float(peso_str)
                    
                    datos.append({"nombre": nombre, "peso": peso})
                except (IndexError, ValueError) as e:
                    print(f"Error al parsear línea en TXT: {linea}")
                    
    except IOError:
        print(f"Error al cargar el archivo: {nombre_archivo}")
        
    return datos

def guardar_en_txt(datos_a_guardar):

    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("---- REGISTRO PESO ----\n")
            
            for dato in datos_a_guardar:
                linea = f"{dato['nombre']}, {dato['peso']} Kg\n" 
                archivo.write(linea)
        
        return True
    except IOError:
        return False