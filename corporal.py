import tkinter as tk

nombre_archivo = "datos-peso-corporal.txt"

datos_guardados = []   

def guardar_datos():

    nombre = entrada_nombre.get()
    peso_texto = entrada_peso.get()
    
    if not nombre or not peso_texto:
        resultado.config(text="Completame ambos campos")
        return
    
    try:
        peso = float(peso_texto)
        
        peso_minimo = 2.0
        peso_maximo = 300.0
        
        if peso < peso_minimo or peso > peso_maximo:
            resultado.config(text=f"El peso debe estar entre {peso_minimo} y {peso_maximo} kg")
            return
        
        datos = {
            "nombre": nombre,
            "peso": peso
        }
        datos_guardados.append(datos)
        guardar_en_txt()
        
        resultado.config(text="Datos guardados correctamente")
        
        entrada_nombre.delete(0, 'end')
        entrada_peso.delete(0, 'end')
        
        mostrar_datos()
        
    except ValueError:
        resultado.config(text="Ingresa un peso válido (número)")
        
def guardar_en_txt():
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("---- REGISTRO PESO ----\n")
            
            for dato in datos_guardados:
                linea = f"{dato['nombre']}, {dato['peso']} Kg\n"
                archivo.write
    except IOError:
        resultado.config(text="Error al escribir el archivo TXT") 

def mostrar_datos():
    
    if not datos_guardados:
        lista_datos.config(text="No hay datos guardados")
        return
    
    texto_datos = "Datos guardados:\n\n"
    for i, dato in enumerate(datos_guardados, 1):
        texto_datos += f"{i}. Nombre: {dato['nombre']} - Peso: {dato['peso']} kg\n"
    
    lista_datos.config(text=texto_datos)



ventana = tk.Tk()
ventana.title("Peso Corporal")
ventana.geometry("400x350")

titulo = tk.Label(ventana, text="Registro Peso Corporal", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

frame_nombre = tk.Frame(ventana)
frame_nombre.pack(pady=5)

label_nombre = tk.Label(frame_nombre, text="Nombre completo:")
label_nombre.pack(side=tk.LEFT)

entrada_nombre = tk.Entry(frame_nombre, width=30)
entrada_nombre.pack(side=tk.LEFT, padx=5)

frame_peso = tk.Frame(ventana)
frame_peso.pack(pady=5)

label_peso = tk.Label(frame_peso, text="Peso (kg):")
label_peso.pack(side=tk.LEFT)

entrada_peso = tk.Entry(frame_peso, width=15)
entrada_peso.pack(side=tk.LEFT, padx=5)

info_peso = tk.Label(ventana, text="Rango válido: 2.0 kg - 300.0 kg", font=("Arial", 10), fg="blue")
info_peso.pack(pady=5)

boton_guardar = tk.Button(ventana, text="Guardar Datos", command=guardar_datos, bg="green", fg="white")
boton_guardar.pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 10))
resultado.pack(pady=5)

lista_datos = tk.Label(ventana, text="No hay datos guardados", justify=tk.LEFT, font=("Arial", 10))
lista_datos.pack(pady=10)

ventana.mainloop()