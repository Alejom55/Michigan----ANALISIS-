import tkinter as tk

ventana_principal = tk.Tk()
ventana_principal.geometry("400x300")
ventana_principal.title("")

def calcular_ecuacion():
    k_1 = eval(tb_k_1.get())
    r_1 = eval(tb_r_1.get())
    k_2 = eval(tb_k_2.get())
    r_2 = eval(tb_r_2.get())
    n = eval(tb_n.get())
    resultado = (k_1 * r_1**n) + (k_2 * r_2**n)
    lb_resultado2.config(text=int(resultado))

lb_ecuacion = tk.Label(ventana_principal, text="k₁r₂^n + k₂r₂^n", font=("", 11))
lb_ecuacion.grid(row=0,column=1)
lb_k_1 = tk.Label(ventana_principal, text="Ingrese k₁:")
lb_k_1.grid(row=1,column=0)
lb_r_1 = tk.Label(ventana_principal, text="Ingrese k₂:")
lb_r_1.grid(row=2,column=0)
lb_k_2 = tk.Label(ventana_principal, text="Ingrese r₁:")
lb_k_2.grid(row=3,column=0)
lb_r_2 = tk.Label(ventana_principal, text="Ingrese r₂:")
lb_r_2.grid(row=4,column=0)
lb_n = tk.Label(ventana_principal, text="Ingrese n:")
lb_n.grid(row=5,column=0)


tb_k_1 = tk.Entry(ventana_principal)
tb_k_1.grid(row=1,column=1)
tb_k_2 = tk.Entry(ventana_principal)
tb_k_2.grid(row=2,column=1)
tb_r_1 = tk.Entry(ventana_principal)
tb_r_1.grid(row=3,column=1)
tb_r_2 = tk.Entry(ventana_principal)
tb_r_2.grid(row=4,column=1)
tb_n = tk.Entry(ventana_principal)
tb_n.grid(row=5,column=1)


lb_resultado = tk.Label(ventana_principal, text="Resultado:")
lb_resultado.grid(row=6,column=0)

lb_resultado2 = tk.Label(ventana_principal, text="")
lb_resultado2.grid(row=6,column=1)

btn_calcular = tk.Button(ventana_principal, text="Calcular", command=calcular_ecuacion)
btn_calcular.grid(row=7,column=0)


ventana_principal.mainloop()
