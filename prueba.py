import tkinter as tk

def suma():
    try:
        n1 = int(numero1.get())
        n2 = int(numero2.get())
        res = n1+n2
        resultado.config(text=f"Resultado: {res}")
    except:
        resultado.config(text=f"Añade solo numeros enteros")


formulario = tk.Tk()
formulario.title("Peso corporal")
formulario.geometry("400x400")

numero1 = tk.StringVar()
numero2 = tk.StringVar()

tk.Label(formulario, text="Numero 1: ").pack(pady=10)
tk.Entry(formulario, textvariable=numero1, width=50).pack(pady=5)

tk.Label(formulario, text="Numero 2: ").pack(pady=10)
tk.Entry(formulario, textvariable=numero2, width=50).pack(pady=5)

tk.Button(formulario, text="suma", command=suma, bg="blue", fg="white").pack(pady=20)

resultado = tk.Label(formulario, text="Resultado: ")
resultado.pack(pady=20)

formulario.mainloop()