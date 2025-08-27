from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")


Frame_tela = Frame(janela, width=235, height=50)
Frame_tela.grid(row=0, column=0)

janela.mainloop()
