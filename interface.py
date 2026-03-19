import tkinter as tk 
from temperatura import Temperatura

def iniciar_interface():

    def converter():
        c = float(entrada_c.get())
        f = float(entrada_f.get())
        k = float(entrada_k.get())

        temp = Temperatura(c, f, k)

        resultado.set(
            f"{c}°C -> {(c * 1.8) + 32:.2f}°F.\n"
            f"{f}°F -> {(f - 32) / 1.8:.2f}°C.\n"
            f"{c}°C -> {c + 273.15:.2f}°k.\n"
            f"{k}°K -> {k - 273.15:.2f}°C."
        )

    janela = tk.Tk()
    janela.title("Converter temperaturas")
    janela.geometry("300x250")

    tk.Label(janela, text="Celsius").pack()
    entrada_c = tk.Entry(janela)
    entrada_c.pack()

    tk.Label(janela, text="Fahrenheit").pack()
    entrada_f = tk.Entry(janela)
    entrada_f.pack()

    tk.Label(janela, text="Kelvin").pack()
    entrada_k = tk.Entry(janela)
    entrada_k.pack() 

    tk.Button(janela, text= "Converter", command=converter).pack()

    resultado = tk.StringVar()
    tk.Label(janela, textvariable=resultado).pack()

    janela.mainloop()