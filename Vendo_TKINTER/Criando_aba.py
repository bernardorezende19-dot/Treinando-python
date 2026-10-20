import tkinter as tk

def constroi_label(texto: str = "Padrão"): 
    ola = tk.Label(text=texto)
    ola.pack()
if __name__ == "__main__":
    janela = tk.Tk()
    constroi_label()
    janela.mainloop()