import os

# Define el directorio y archivo
directorio = "datos"
nombre_archivo = "datos-peso-corporal.txt"

# Crea la ruta completa
ruta_completa = os.path.join(directorio, nombre_archivo)

def cargar_desde_txt():
    datos = []
    
    # Si no existe el directorio, lo crea
    if not os.path.exists(directorio):
        os.makedirs(directorio)
        return datos
    
    if not os.path.exists(ruta_completa):
        return datos

    try:
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            archivo.readline()  # Saltar encabezado
            
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
                except (IndexError, ValueError):
                    print(f"Error al parsear línea: {linea}")
                    
    except IOError as e:
        print(f"Error al cargar el archivo: {e}")
        
    return datos

def guardar_en_txt(datos_a_guardar):
    try:
        # Asegurar que el directorio existe
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        
        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            archivo.write("---- REGISTRO PESO ----\n")
            
            for dato in datos_a_guardar:
                linea = f"{dato['nombre']}, {dato['peso']} Kg\n"
                archivo.write(linea)
        
        return True
    except IOError as e:
        print(f"Error al guardar: {e}")
        return False