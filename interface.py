import tkinter as tk 
from temperatura import Temperatura

def iniciar_interface():

    def verificar(event, campo_atual, proxiomo_campo):
        valor = campo_atual.get().strip()

        if valor == "":
            resultado.set("Digite apenas números.")
            return "break"
        
        try:
            float(valor)
            proxiomo_campo.focus()
        except:
            resultado.set("Digite apenas números.")
            return "break"

    def converter():
        try:
            c = float(entrada_c.get())
            f = float(entrada_f.get())
            ck = float(entrada_ck.get())
            k = float(entrada_k.get())
        except:
            return

        temp = Temperatura(c, f, ck, k )

        resultado.set(
            f"{c}°C -> {(c * 1.8) + 32:.2f}°F.\n"
            f"{f}°F -> {(f - 32) / 1.8:.2f}°C.\n"
            f"{ck}°C -> {ck + 273.15:.2f}°k.\n"
            f"{k}°K -> {k - 273.15:.2f}°C."
        )

    janela = tk.Tk()
    janela.title("Converter temperaturas")
    janela.geometry("300x250")

    tk.Label(janela, text="Celsius para Fahtenheit").pack()
    entrada_c = tk.Entry(janela)
    entrada_c.pack()
    entrada_c.bind("<Return>", lambda e: verificar(e, entrada_c, entrada_f))

    tk.Label(janela, text="Fahrenheit para Celsius").pack()
    entrada_f = tk.Entry(janela)
    entrada_f.pack()
    entrada_f.bind("<Return>", lambda e: verificar(e, entrada_f, entrada_ck))

    tk.Label(janela, text="Celsius para Kelvin").pack()
    entrada_ck = tk.Entry(janela)
    entrada_ck.pack()
    entrada_ck.bind("<Return>", lambda e: verificar(e, entrada_ck, entrada_k))

    tk.Label(janela, text="Kelvin para Celsius").pack()
    entrada_k = tk.Entry(janela)
    entrada_k.pack()
    janela.bind("<Return>", lambda e: converter())

    tk.Button(janela, text= "Converter", command=converter).pack()

    resultado = tk.StringVar()
    tk.Label(janela, textvariable=resultado).pack()

    janela.mainloop()