import tkinter as tk
from tkinter import HORIZONTAL, VERTICAL, ttk, messagebox
from contratado_dao import Contratado, borrar_tabla, buscar, crear_tabla, editar, eliminar, guadar, listar


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu,width=500, height=500)

    menu_inicio= tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label='inicio', menu= menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command= root.destroy)


#interfaz del programa 
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=500, height=500)
        self.root= root
        self.pack()
        # self.config( bg='#B4F6B3')
        self.id_contratado= None

        self.campos_contratos()
        self.deshabilitar_campos()
        self.tabla_contratado()

    def campos_contratos(self):
        #nombre de cada campo
        self.label_nombre = tk.Label(self, text= 'Nombre: ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row= 0, column = 0, padx=3, pady=5)

        self.label_cuil = tk.Label(self, text= 'Cuil: ')
        self.label_cuil.config(font= ('Arial', 12, 'bold'))
        self.label_cuil.grid(row= 1, column = 0 , padx=3, pady=5)

        self.label_nacimiento = tk.Label(self, text= 'Fecha de Nacimiento: ')
        self.label_nacimiento.config(font= ('Arial', 12, 'bold'))
        self.label_nacimiento.grid(row= 2, column = 0 , padx=5, pady=5)

        self.label_monto = tk.Label(self, text= 'Monto Inicial: ')
        self.label_monto.config(font= ('Arial', 12, 'bold'))
        self.label_monto.grid(row= 3, column = 0 , padx=5, pady=5)

        self.label_modificacion = tk.Label(self, text= 'Modificacion: ')
        self.label_modificacion.config(font= ('Arial', 12, 'bold'))
        self.label_modificacion.grid(row= 4, column = 0 , padx=5, pady=5)

        self.label_duracion = tk.Label(self, text= 'Duración de la modificacion: ')
        self.label_duracion.config(font= ('Arial', 12, 'bold'))
        self.label_duracion.grid(row= 5, column = 0, padx=5, pady=5)

        self.label_area_de_trabajo = tk.Label(self, text= 'Área de Trabajo: ')
        self.label_area_de_trabajo.config(font= ('Arial', 12, 'bold'))
        self.label_area_de_trabajo.grid(row= 6, column = 0 , padx=5, pady=5)

        self.label_funcion = tk.Label(self, text= 'funcion: ')
        self.label_funcion.config(font= ('Arial', 12, 'bold'))
        self.label_funcion.grid(row= 7, column = 0 , padx=5, pady=5 )

        self.label_domicilio = tk.Label(self, text= 'domicilio: ')
        self.label_domicilio.config(font= ('Arial', 12, 'bold'))
        self.label_domicilio.grid(row= 8, column = 0, padx=5, pady=5)

        self.label_telefono = tk.Label(self, text= 'telefono: ')
        self.label_telefono.config(font= ('Arial', 12, 'bold'))
        self.label_telefono.grid(row= 9, column = 0, padx=4, pady=5)

        self.label_mail = tk.Label(self, text= 'mail: ')
        self.label_mail.config(font= ('Arial', 12, 'bold'))
        self.label_mail.grid(row= 10, column = 0, padx=5, pady=5)

        self.label_otros_trabajos = tk.Label(self, text= 'Otros Trabajos: ')
        self.label_otros_trabajos.config(font= ('Arial', 12, 'bold'))
        self.label_otros_trabajos.grid(row= 11, column = 0, padx=5, pady=5)


        #Entradas de cada campo
        self.mi_nombre= tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width= 70,  font= ('Arial', 12))
        self.entry_nombre.grid(row= 0, column = 1, padx=5, pady=5 ,columnspan= 2)

        self.mi_cuil= tk.StringVar()
        self.entry_cuil = tk.Entry(self, textvariable= self.mi_cuil)
        self.entry_cuil.config(width= 70,   font= ('Arial', 12))
        self.entry_cuil.grid(row= 1, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_nacimiento= tk.StringVar()
        self.entry_nacimiento = tk.Entry(self,textvariable= self.mi_nacimiento)
        self.entry_nacimiento.config(width= 70, font= ('Arial', 12))
        self.entry_nacimiento.grid(row= 2, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_monto= tk.StringVar()
        self.entry_monto = tk.Entry(self, textvariable= self.mi_monto)
        self.entry_monto.config(width= 70,  font= ('Arial', 12))
        self.entry_monto.grid(row= 3, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_modificacion= tk.StringVar()
        self.entry_modificacion = tk.Entry(self, textvariable= self.mi_modificacion)
        self.entry_modificacion.config(width= 70, font= ('Arial', 12))
        self.entry_modificacion.grid(row= 4, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_duracion= tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable= self.mi_duracion)
        self.entry_duracion.config(width= 70,font= ('Arial', 12))
        self.entry_duracion.grid(row= 5, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_area_de_trabajo= tk.StringVar()
        self.entry_area_de_trabajo = tk.Entry(self, textvariable= self.mi_area_de_trabajo)
        self.entry_area_de_trabajo.config(width= 70,font= ('Arial', 12))
        self.entry_area_de_trabajo.grid(row= 6, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_funcion= tk.StringVar()
        self.entry_funcion = tk.Entry(self, textvariable= self.mi_funcion)
        self.entry_funcion.config(width= 70, font= ('Arial', 12))
        self.entry_funcion.grid(row= 7, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_domicilio= tk.StringVar()
        self.entry_domicilio = tk.Entry(self, textvariable= self.mi_domicilio)
        self.entry_domicilio.config(width= 70,font= ('Arial', 12))
        self.entry_domicilio.grid(row= 8, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_telefono= tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable= self.mi_telefono)
        self.entry_telefono.config(width= 70, font= ('Arial', 12))
        self.entry_telefono.grid(row= 9, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_mail= tk.StringVar()
        self.entry_mail = tk.Entry(self, textvariable= self.mi_mail)
        self.entry_mail.config(width= 70,  font= ('Arial', 12))
        self.entry_mail.grid(row= 10, column = 1, padx=5, pady=5,columnspan= 2)

        self.mi_otros_trabajos= tk.StringVar()
        self.entry_otros_trabajos = tk.Entry(self, textvariable= self.mi_otros_trabajos)
        self.entry_otros_trabajos.config(width= 70,font= ('Arial', 12))
        self.entry_otros_trabajos.grid(row= 11, column = 1, padx=5, pady=5,columnspan= 2)


        # self.mi_buscar=tk.StringVar()
        # self.entry_buscar = tk.Entry(self, textvariable= self.mi_buscar)
        # self.entry_buscar.config(width= 70,font= ('Arial', 12))
        # self.entry_buscar.grid(row= 12, column = 1, padx=5, pady=5,columnspan= 2)


      #Botones
        self.boton_nuevo= tk.Button(self, text= "Nuevo", command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font= ('Arial', 12, 'bold'), fg= '#FFFFFF', bg='#1CAA23', cursor='hand2', activebackground= '#F5F9F5' )
        self.boton_nuevo.grid(row=12, column=0, padx=5, pady=5 )

        self.boton_guardar= tk.Button(self, text= "Guardar", command= self.guardar_datos)
        self.boton_guardar.config(width=20, font= ('Arial', 12, 'bold'), fg= '#FFFFFF', bg='#070BFA', cursor='hand2', activebackground= '#F5F9F5' )
        self.boton_guardar.grid(row=12, column=1, padx=5, pady=5)
        #este es el boton guardar, que esta creado, pero no funciona 
        self.boton_buscar= tk.Button(self, text= "Buscar", command= buscar)
        self.boton_buscar.config(width=20, font= ('Arial', 12, 'bold'), fg= '#FFFFFF', bg='#EE7F08', cursor='hand2', activebackground= '#F5F9F5' )
        self.boton_buscar.grid(row=12, column=2, padx=5, pady=5)

        self.boton_cancelar= tk.Button(self, text= "Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font= ('Arial', 12, 'bold'), fg= '#FFFFFF', bg='#FA1007', cursor='hand2', activebackground= '#F5F9F5' )
        self.boton_cancelar.grid(row=12, column=3, padx=5, pady=5)


       


    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_cuil.set('')
        self.mi_nacimiento.set('')
        self.mi_monto.set('')
        self.mi_modificacion.set('')
        self.mi_duracion.set('')
        self.mi_area_de_trabajo.set('')
        self.mi_funcion.set('')
        self.mi_domicilio.set('')
        self.mi_telefono.set('')
        self.mi_mail.set('')
        self.mi_otros_trabajos.set('')


        self. entry_nombre.config(state='normal')
        self. entry_cuil.config(state='normal')
        self. entry_nacimiento.config(state='normal')
        self. entry_monto.config(state='normal')
        self. entry_modificacion.config(state='normal')
        self. entry_duracion.config(state='normal')
        self. entry_area_de_trabajo.config(state='normal')
        self. entry_funcion.config(state='normal')
        self. entry_domicilio.config(state='normal')
        self. entry_telefono.config(state='normal')
        self. entry_mail.config(state='normal')
        self. entry_otros_trabajos.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_contratado= None

        self.mi_nombre.set('')
        self.mi_cuil.set('')
        self.mi_nacimiento.set('')
        self.mi_monto.set('')
        self.mi_modificacion.set('')
        self.mi_duracion.set('')
        self.mi_area_de_trabajo.set('')
        self.mi_funcion.set('')
        self.mi_domicilio.set('')
        self.mi_telefono.set('')
        self.mi_mail.set('')
        self.mi_otros_trabajos.set('')



        self. entry_nombre.config(state='disabled')
        self. entry_cuil.config(state='disabled')
        self. entry_nacimiento.config(state='disabled')
        self. entry_monto.config(state='disabled')
        self. entry_modificacion.config(state='disabled')
        self. entry_duracion.config(state='disabled')
        self. entry_area_de_trabajo.config(state='disabled')
        self. entry_funcion.config(state='disabled')
        self. entry_domicilio.config(state='disabled')
        self. entry_telefono.config(state='disabled')
        self. entry_mail.config(state='disabled')
        self. entry_otros_trabajos.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):

        self.contratado =Contratado(
            self.mi_nombre.get(),
            self.mi_cuil.get(),
            self.mi_nacimiento.get(),
            self.mi_monto.get(),
            self.mi_modificacion.get(),
            self.mi_duracion.get(),
            self.mi_area_de_trabajo.get(),
            self.mi_funcion.get(),
            self.mi_domicilio.get(),
            self.mi_telefono.get(),
            self.mi_mail.get(),
            self.mi_otros_trabajos.get(),
        )

        if self.id_contratado== None:
            guadar(self.contratado)
        
       
        else:
           editar(self.contratado, self.id_contratado)
           
        
        self.tabla_contratado()

          #deshabilitar compoos
        self.deshabilitar_campos()

      
    def tabla_contratado(self):

        #Recuperar la lista de contratado
        self.lista_contratado= listar()
        self.lista_contratado.reverse()

        # Organizo el Treeview y las barras de scroll en una nueva Frame
        # para que sea mas facil configurar el layout
        self._frametabla = ttk.Frame(self)
        self._frametabla.grid(row=13, column= 0, columnspan= 5, sticky = 'nse')
        columnas = ('Nombre','Cuil', 'Fecha de Nacimiento', 
                    'Monto Inicial','modificacion', 'Duración de la modificacion',
                    'Área de Trabajo', 'funcion','domicilio','telefono', 'mail', 'Otros Trabajos')
        self.tabla= ttk.Treeview(self._frametabla, column=columnas)
        self.tabla.grid(row=0, column=0)
        
        # Inicialmente le configuro ancho de columnas pequeño para que
        # no ocupe mas del tamaño de pantalla configurado.
        total_columnas = len(columnas)
        for i in range(0, total_columnas):
            self.tabla.column(i, width=100)
        self.tabla.grid(row=0, column=0)
        
        # Un Segundo despues de que se muestre en pantalla,
        # redimensiono las columnas
        def redimensionar_columnas():
            self.tabla.column("#0", minwidth=100)
            for i in range(0, total_columnas):
                self.tabla.column(i, minwidth=200)
        
        self.tabla.after(1000, redimensionar_columnas)

        #scrollbar vertical 
        
        self.scroll = ttk.Scrollbar(self._frametabla,
        orient = VERTICAL , command = self.tabla.yview)
        self.scroll.grid(row=0, column=1, sticky="ns")
        self.tabla.configure(yscrollcommand = self.scroll.set)

         #scrollbar horizontal
        self.ladox = ttk.Scrollbar(self._frametabla,
        orient = HORIZONTAL, command = self.tabla.xview)
        self.ladox.grid(row = 1, column=0, sticky = 'ew')
        self.tabla.configure(xscrollcommand= self.ladox.set)


        self.tabla.heading('#0', text= 'ID')
        self.tabla.heading('#1', text= 'NOMBRE')
        self.tabla.heading('#2', text= 'CUIL')
        self.tabla.heading('#3', text= 'FECHA DE NACIMIENTO')
        self.tabla.heading('#4', text= 'MONTO INICIAL')
        self.tabla.heading('#5', text= 'MODIFICACIÓN')
        self.tabla.heading('#6', text= 'DURACIÓN DE LA MODIFICACIÓN')
        self.tabla.heading('#7', text= 'ÁREA DE TRABAJO')
        self.tabla.heading('#8', text= 'FUNCIÓN')
        self.tabla.heading('#9', text= 'DOMICILIO')
        self.tabla.heading('#10', text= 'TELÉFONO')
        self.tabla.heading('#11', text= 'MAIL')
        self.tabla.heading('#12', text= 'OTROS TRABAJOS')

        #iterar la lista de contratos
        for p in self.lista_contratado:
            self.tabla.insert('', 0, text= p[0],
            values=(p[1], p[2],p[3],p[4], p[5], p[6], p[7],p[8],p[9], p[10],p[11],p[12]))

        self.boton_editar= tk.Button(self, text= "Editar", command= self.editar_datos)
        self.boton_editar.config(width=20, font= ('Arial', 12, 'bold'),
                                 fg= '#FFFFFF', bg='#1CAA23', cursor='hand2', activebackground= '#F5F9F5' )
        self.boton_editar.grid(row=12, column=4, padx=5, pady=5)


        self.boton_eliminar= tk.Button(self, text= "Eliminar", command= self.eliminar_datos)
        self.boton_eliminar.config(width=20, font= ('Arial', 12, 'bold'), fg= '#FFFFFF', 
                                   bg='#FA1007', cursor='hand2', activebackground= '#F5F9F5' )
        self.boton_eliminar.grid(row=11, column=4, padx=5, pady=5)

    def editar_datos (self):
        try:
            self.id_contratado = self.tabla.item(self.tabla.selection())['text']
            self.nombre_contratado = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.cuil_contratado = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.nacimiento_contratado = self.tabla.item(
                self.tabla.selection())['values'][2]
            self.monto_contratado = self.tabla.item(
                self.tabla.selection())['values'][3]
            self.modificacion_contratado = self.tabla.item(
                self.tabla.selection())['values'][4]
            self.duracion_contratado = self.tabla.item(
                self.tabla.selection())['values'][5]
            self.area_de_trabajo_contratado = self.tabla.item(
                self.tabla.selection())['values'][6]
            self.funcion_contratado = self.tabla.item(
                self.tabla.selection())['values'][7]
            self.domicilio_contratado = self.tabla.item(
                self.tabla.selection())['values'][8]
            self.telefono_contratado = self.tabla.item(
                self.tabla.selection())['values'][9]
            self.mail_contratado = self.tabla.item(
                self.tabla.selection())['values'][10]
            self.otros_trabajos_contratado = self.tabla.item(
                self.tabla.selection())['values'][11]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_contratado)
            self.entry_cuil.insert(0, self.Cuil_contratado)
            self.entry_nacimiento.insert(0, self.nacimiento_pelicula)
            self.entry_monto.insert(0, self.monto_contratado)
            self.entry_modificacion.insert(0, self.modificacion_contratado)
            self.entry_duracion.insert(0, self.duracion_contratado)
            self.entry_area_de_trabajo.insert(0, self.area_de_trabajo_contratado)
            self.entry_funcion.insert(0, self.funcion_contratado)
            self.entry_domicilio.insert(0, self.domicilio_contratado)
            self.entry_telefono.insert(0, self.telefono_contratado)
            self.entry_mail.insert(0, self.mail_contratado)
            self.entry_otros_trabajos.insert(0, self.otros_trabajos_contratado)


        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado nigun registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_contratado = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_contratado)

            self.tabla_contratado()
            self.id_contratado = None
        except:
            titulo = 'Eliminar un Registro'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
    
            
        # acá se deberia realizar la funcionalidad de botón buscar que se deberia poner el cuil del contratado y que te devuelva todo los campos 
    # def busca(self):
    #     try:
    #         self.id_contratado = self.tabla.item(self.tabla.selection())['text']
    #         self.nombre_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][0]
    #         self.cuil_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][1]
    #         self.nacimiento_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][2]
    #         self.monto_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][3]
    #         self.modificacion_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][4]
    #         self.duracion_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][5]
    #         self.area_de_trabajo_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][6]
    #         self.funcion_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][7]
    #         self.domicilio_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][8]
    #         self.telefono_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][9]
    #         self.mail_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][10]
    #         self.otros_trabajos_contratado = self.tabla.item(
    #             self.tabla.selection())['values'][11]

    #         self.habilitar_campos()

    #         self.entry_nombre.insert(0, self.nombre_contratado)
    #         self.entry_cuil.insert(0, self.Cuil_contratado)
    #         self.entry_nacimiento.insert(0, self.nacimiento_pelicula)
    #         self.entry_monto.insert(0, self.monto_contratado)
    #         self.entry_modificacion.insert(0, self.modificacion_contratado)
    #         self.entry_duracion.insert(0, self.duracion_contratado)
    #         self.entry_area_de_trabajo.insert(0, self.area_de_trabajo_contratado)
    #         self.entry_funcion.insert(0, self.funcion_contratado)
    #         self.entry_domicilio.insert(0, self.domicilio_contratado)
    #         self.entry_telefono.insert(0, self.telefono_contratado)
    #         self.entry_mail.insert(0, self.mail_contratado)
    #         self.entry_otros_trabajos.insert(0, self.otros_trabajos_contratado)


    #     except:
    #         titulo = 'Busqueda de contrtado'
    #         mensaje = 'No se ha podido encontarar este registro'
    #         messagebox.showerror(titulo, mensaje)
