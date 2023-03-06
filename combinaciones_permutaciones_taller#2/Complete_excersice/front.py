import tkinter as tk
from tkinter import ttk
from combinatoria import *


root = tk.Tk()
root.title("Combinatoria")

def mostrar_textbox():
    if combo.get() == "Permutacion ordinaria":
        label_m.grid(row=1, column=0)
        tb_m.grid(row=1, column=1)
        label_n.grid_forget()
        tb_n.grid_forget()
    else:
        label_m.grid(row=1, column=0)
        tb_m.grid(row=1, column=1)
        label_n.grid(row=2, column=0)
        tb_n.grid(row=2, column=1)


def calcular(combinatoria_seleccionada, m, n):
    if combinatoria_seleccionada == "Combinacion con repeticion":
        resultado = combinacion_con_repeticion(m,n)
        lb_variable_resultado.config(text=resultado)
    elif combinatoria_seleccionada == "Combinacion ordinaria":
        resultado = combinacion_ordinaria(m,n)
        lb_variable_resultado.config(text=resultado)
    elif combinatoria_seleccionada == "Permutacion con repeticion":
        resultado = permutacion_con_repeticion(m,n)
        lb_variable_resultado.config(text=resultado)
    elif combinatoria_seleccionada == "Permutacion ordinaria":
        resultado = permutacion_ordinaria(m)
        lb_variable_resultado.config(text= resultado)
    elif combinatoria_seleccionada == "Variacion con repeticion":
        resultado = variaciones_con_repeticion(m,n)
        lb_variable_resultado.config(text=resultado)
    elif combinatoria_seleccionada == "Variacion ordinaria":
        resultado = variacion_ordinaria(m,n)
        lb_variable_resultado.config(text=resultado)
    return resultado

def suma():
    respuesta = 0
    numero1 = float(lb_variable_resultado.cget("text"))
    numero2 = calcular(combo.get(),int(tb_m.get()),int(tb_n.get()))
    respuesta = numero1 + numero2
    lb_variable_resultado.config(text=int(respuesta))

def multiplicacion():
    respuesta = 1
    numero1 = float(lb_variable_resultado.cget("text"))
    numero2 = calcular(combo.get(),int(tb_m.get()),int(tb_n.get()))
    respuesta = numero1 * numero2
    lb_variable_resultado.config(text=int(respuesta))

def borrar():
    lb_variable_resultado.config(text="")
    tb_m.delete(0, tk.END)
    tb_n.delete(0, tk.END)

# Establecer un tamaño predeterminado de 400x300 píxeles
root.geometry("450x300")


# Crear una lista de opciones para el Combobox
opciones = ["Combinacion con repeticion", "Combinacion ordinaria", "Permutacion con repeticion",
            "Permutacion ordinaria", "Variacion con repeticion", "Variacion ordinaria"]

# Crear un Combobox y asociarlo con las opciones
combo = ttk.Combobox(root, values=opciones, state="readonly", width=len(max(opciones, key=len)))
combo.set("")
combo.pack()
combo.grid(row=0, column=1)


#Label que esta al lado de las opciones de combinatorias
label = tk.Label(root, text="Elija una opción:")
label.grid(row=0, column=0)

#Aqui se crea m y n, y el lb del resultado
label_m = tk.Label(root, text="Ingrese un valor de m:")
tb_m = tk.Entry(root)

label_n = tk.Label(root, text="Ingrese un valor de n:")
tb_n = tk.Entry(root)

lb_resultado = tk.Label(root, text="Resultado:")
lb_resultado.grid(row=4,column=3)

lb_variable_resultado = tk.Label(root, text="")
lb_variable_resultado.grid(row=4,column=4)

#Aqui se crea los botones de la suma,multipliacion y calcular

btn_calcular_todos = tk.Button(root, text="Calcular",command=lambda: calcular(combo.get(),int(tb_m.get()),int(tb_n.get())), width=11)
btn_calcular_todos.grid(row=5,column=3)


btn_calcular_suma = tk.Button(root, text="Sumar",command=lambda: suma(),width=11)
btn_calcular_suma.grid(row=6,column=3)

btn_calcular_multiplicacion = tk.Button(root, text="Multiplicacion",command=lambda: multiplicacion(),width=11)
btn_calcular_multiplicacion.grid(row=7,column=3)

btn_borrar = tk.Button(root, text="Borrar",command=lambda: borrar(),width=11)
btn_borrar.grid(row=8,column=3)

# Vincular el evento de selección a la función para mostrar/ocultar el Label y el Entry
combo.bind("<<ComboboxSelected>>", lambda event: mostrar_textbox())

root.mainloop()
