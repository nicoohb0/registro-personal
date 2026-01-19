import os

directorio = "datos"
nombre_archivo = "datos-peso-corporal.txt"

ruta_completa = os.path.join(directorio, nombre_archivo)

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal"""
    if altura <= 0:
        return 0
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """Clasifica el IMC según categorías estándar"""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad grado I"
    elif imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def cargar_desde_txt():
    datos = []
    
    if not os.path.exists(directorio):
        os.makedirs(directorio)
        return datos
    
    if not os.path.exists(ruta_completa):
        return datos

    try:
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            archivo.readline()
            
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                
                try:
                    partes = linea.split(',')
                    nombre = partes[0].strip()
                    peso_str = partes[1].strip().replace(" Kg", "")
                    altura_str = partes[2].strip().replace(" m", "")
                    imc_str = partes[3].strip().replace(" IMC:", "")
                    clasificacion = partes[4].strip()
                    
                    peso = float(peso_str)
                    altura = float(altura_str)
                    imc = float(imc_str)
                    
                    datos.append({
                        "nombre": nombre, 
                        "peso": peso, 
                        "altura": altura,
                        "imc": imc,
                        "clasificacion": clasificacion
                    })
                except (IndexError, ValueError):
                    print(f"Error al parsear línea: {linea}")
                    
    except IOError as e:
        print(f"Error al cargar el archivo: {e}")
        
    return datos

def guardar_en_txt(datos_a_guardar):
    try:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        
        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            archivo.write("---- REGISTRO PESO Y IMC ----\n")
            
            for dato in datos_a_guardar:
                linea = f"{dato['nombre']}, {dato['peso']} Kg, {dato['altura']} m, IMC:{dato['imc']}, {dato['clasificacion']}\n"
                archivo.write(linea)
        
        return True
    except IOError as e:
        print(f"Error al guardar: {e}")
        return False