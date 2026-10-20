import tkinter as tk

janela = tk.Tk()
label = tk.Label(
    text= "Brincando com Tkinter",
    foreground="red",#da pra usar hexadecimal
    background="black"
)
label.pack()

janela.mainloop()