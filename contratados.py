import tkinter as tk 
from tkinter import ttk
from gui_app import Frame, barra_menu



def main():
    root = tk.Tk()
    root.title('CONTRATADOS MUNICIPALIDAD DE LA PAZ')
    root.iconbitmap ( 'img/logo.ico')
    # root.resizable(0,0)
    root.geometry('1400x1100')
    root.minsize(width=1400, height=1100)
    barra_menu(root)

    app = Frame(root = root)
    app.mainloop()
   

if __name__ == '__main__':
  main()