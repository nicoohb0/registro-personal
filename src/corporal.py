import tkinter as tk
from crear_fichero import cargar_desde_txt, guardar_en_txt

datos_guardados = []   

def validar_nombre(nuevo_texto):
    if len(nuevo_texto) > 15:
        return False
    if nuevo_texto == "":
        return True
    return nuevo_texto.replace(" ", "").isalpha()

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

def guardar_datos():
    nombre = entrada_nombre.get().strip()
    peso_texto = entrada_peso.get()
    altura_texto = entrada_altura.get()
    
    if not nombre or not peso_texto or not altura_texto:
        resultado.config(text="Completa todos los campos")
        return
    
    try:
        peso = float(peso_texto)
        altura = float(altura_texto)
        
        peso_minimo = 2.0
        peso_maximo = 300.0
        altura_minima = 0.5
        altura_maxima = 2.5
        
        if peso < peso_minimo or peso > peso_maximo:
            resultado.config(text=f"El peso debe estar entre {peso_minimo} y {peso_maximo} kg")
            return
        
        if altura < altura_minima or altura > altura_maxima:
            resultado.config(text=f"La altura debe estar entre {altura_minima} y {altura_maxima} m")
            return
        
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)
        
        datos = {
            "nombre": nombre,
            "peso": peso,
            "altura": altura,
            "imc": round(imc, 2),
            "clasificacion": clasificacion
        }
        datos_guardados.append(datos)
        
        if guardar_en_txt(datos_guardados):
            resultado.config(text="Datos guardados correctamente y en el fichero")
        else:
            resultado.config(text="Datos guardados, pero error al guardar en el fichero")
        
        mostrar_info_imc(imc, clasificacion)
        
        entrada_nombre.delete(0, 'end')
        entrada_peso.delete(0, 'end')
        entrada_altura.delete(0, 'end')
        
        mostrar_datos()
        
    except ValueError:
        resultado.config(text="Ingresa valores válidos (números)")

def mostrar_info_imc(imc, clasificacion):
    """Muestra la información del IMC calculado"""
    texto_imc = f"IMC calculado: {imc:.2f} - {clasificacion}"
    label_imc_resultado.config(text=texto_imc)
    
    if clasificacion == "Peso normal":
        label_imc_resultado.config(fg="green")
    elif clasificacion in ["Bajo peso", "Sobrepeso"]:
        label_imc_resultado.config(fg="orange")
    else:
        label_imc_resultado.config(fg="red")

def mostrar_datos():
    if not datos_guardados:
        lista_datos.config(text="No hay datos guardados")
        return
    
    texto_datos = "Datos guardados:\n\n"
    for i, dato in enumerate(datos_guardados, 1):
        texto_datos += f"{i}. Nombre: {dato['nombre']} - "
        texto_datos += f"Peso: {dato['peso']} kg - "
        texto_datos += f"Altura: {dato['altura']} m - "
        texto_datos += f"IMC: {dato['imc']} ({dato['clasificacion']})\n"
    
    lista_datos.config(text=texto_datos)

datos_guardados = cargar_desde_txt()

ventana = tk.Tk()
ventana.title("Peso Corporal")
ventana.geometry("450x450")

titulo = tk.Label(ventana, text="Registro Peso Corporal", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

frame_nombre = tk.Frame(ventana)
frame_nombre.pack(pady=5)

label_nombre = tk.Label(frame_nombre, text="Nombre completo:")
label_nombre.pack(side=tk.LEFT)

vcmd = (ventana.register(validar_nombre), '%P')
entrada_nombre = tk.Entry(frame_nombre, width=30, validate="key", validatecommand=vcmd)
entrada_nombre.pack(side=tk.LEFT, padx=5)

frame_peso = tk.Frame(ventana)
frame_peso.pack(pady=5)

label_peso = tk.Label(frame_peso, text="Peso (kg):")
label_peso.pack(side=tk.LEFT)

entrada_peso = tk.Entry(frame_peso, width=15)
entrada_peso.pack(side=tk.LEFT, padx=5)

frame_altura = tk.Frame(ventana)
frame_altura.pack(pady=5)

label_altura = tk.Label(frame_altura, text="Altura (m):")
label_altura.pack(side=tk.LEFT)

entrada_altura = tk.Entry(frame_altura, width=15)
entrada_altura.pack(side=tk.LEFT, padx=5)

info_nombre = tk.Label(ventana, text="Nombre: solo letras y espacios, máximo 15 caracteres", 
                       font=("Arial", 9), fg="green")
info_nombre.pack(pady=2)

info_peso = tk.Label(ventana, text="Rango válido peso: 2.0 kg - 300.0 kg", font=("Arial", 9), fg="blue")
info_peso.pack(pady=2)

info_altura = tk.Label(ventana, text="Rango válido altura: 0.5 m - 2.5 m", font=("Arial", 9), fg="blue")
info_altura.pack(pady=2)

boton_guardar = tk.Button(ventana, text="Guardar Datos y Calcular IMC", 
                         command=guardar_datos, bg="grey", fg="black", 
                         font=("Arial", 10, "bold"))
boton_guardar.pack(pady=10)

label_imc_resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
label_imc_resultado.pack(pady=5)

resultado = tk.Label(ventana, text="", font=("Arial", 10))
resultado.pack(pady=5)

lista_datos = tk.Label(ventana, text="No hay datos guardados", justify=tk.LEFT, 
                      font=("Arial", 9))
lista_datos.pack(pady=10)

ventana.mainloop()