import tkinter as tk

class PackFillapp:
    def __init__(self,raiz):
        tamanhos = [(100,"red"), (50, "green"), (25, "blue")]

        for altura, cor in tamanhos:
            frame=tk.Frame(
                raiz, width=altura, height= altura, bg=cor
            )
            frame.pack(fill=tk.X)

if __name__ == "__main__":
    raiz = tk.Tk()
    PackFillapp(raiz)
    raiz.mainloop()