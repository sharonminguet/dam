import tkinter as tk

def diHola():
    etiqueta.config(text="¿Que necesitas?")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Mi Asistente")
    ventana.geometry("300x200")

    global etiqueta
    etiqueta = tk.Label(ventana, text="")
    etiqueta.pack(pady=20)

    boton = tk.Button(ventana, text="Pulsame", padx=15, pady=15, command=diHola)
    boton.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()
