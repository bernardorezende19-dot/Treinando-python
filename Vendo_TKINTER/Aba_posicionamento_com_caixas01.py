import tkinter as tk

class GridApp:
    def __init__(self, raiz):
        for posicao in range(3):
            raiz.columnconfigure(posicao, weight=1, minsize=75)
            raiz.rowconfigure(posicao, weight=1, minsize=50)
        for linha in range(3):
            for coluna in range(3):
                frame = tk.Frame(raiz, relief=tk.RAISED, bd=1)
                frame.grid(row=linha, column=coluna, padx=5, pady=5)
                texto = f"Linha {linha}\nColuna {coluna}"
                tk.Label(frame, text=texto).pack()

if __name__ == "__main__":
    raiz = tk.Tk()
    GridApp(raiz)
    raiz.mainloop()