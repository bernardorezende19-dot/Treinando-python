import tkinter as tk

janela = tk.Tk()
janela.title("Minha janela")

botao1 = tk.Button(
    janela,
    text="Botão 1",
    width=25,
    height=5
)
botao1.pack()

botao2 = tk.Button(
    janela,
    text="Botão 2",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)
botao2.pack()

janela.mainloop()