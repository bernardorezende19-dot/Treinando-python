import tkinter as tk

janela = tk.Tk()
label = tk.Label(
    text= "Brincando com Tkinter",
    foreground="#0000FF",#da pra usar hexadecimal
    background="#00FFFF",
    width=40,#Lagura
    height=40#Altura
)
label.pack()

janela.mainloop()