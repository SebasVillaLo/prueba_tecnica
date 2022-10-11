# Importamos la libreria tkinter para crear la interfaz grafica
import tkinter
import tkinter.messagebox
from calculo import calcular

# Creamos la ventana principal
ventana = tkinter.Tk()
ventana.title("Prueba Tecnica")
ventana.geometry("500x400")
imagen = tkinter.PhotoImage(file="assets/image/logo.png")
min_resize_imagen = imagen.subsample(2, 2)
logo = tkinter.Label(ventana, image=min_resize_imagen)
logo.place(x=300, y=60)


etiqueta = tkinter.Label(
    ventana, text='Ingrese los datos solicitados para calcular el precio de venta del producto')
etiqueta.place(x=10, y=10)
etiqueta = tkinter.Label(ventana, text='Ingrese el nombre del empleado')
etiqueta.place(x=10, y=60)
nombre_empleado_entry = tkinter.Entry(ventana)
nombre_empleado_entry.place(x=13, y=80)
etiqueta = tkinter.Label(ventana, text='Ingrese el nombre de la empresa')
etiqueta.place(x=10, y=110)
nombre_empresa_entry = tkinter.Entry(ventana)
nombre_empresa_entry.place(x=13, y=130)
etiqueta = tkinter.Label(
    ventana, text='Ingrese el nombre del contacto del cliente')
etiqueta.place(x=10, y=160)
nombre_contacto_cliente_entry = tkinter.Entry(ventana)
nombre_contacto_cliente_entry.place(x=13, y=180)
etiqueta = tkinter.Label(
    ventana, text='Ingrese el nombre de la empresa del cliente')
etiqueta.place(x=10, y=210)
nombre_empresa_cliente_entry = tkinter.Entry(ventana)
nombre_empresa_cliente_entry.place(x=13, y=230)
etiqueta = tkinter.Label(ventana, text='Ingrese el costo del producto ($)')
etiqueta.place(x=10, y=260)
costo_producto_entry = tkinter.Entry(ventana)
costo_producto_entry.place(x=13, y=280)
etiqueta = tkinter.Label(ventana, text='Ingrese el margen estimado (%)')
etiqueta.place(x=10, y=310)
margen_estimado_entry = tkinter.Entry(ventana)
margen_estimado_entry.place(x=13, y=330)
boton = tkinter.Button(ventana, text='Calcular', command= lambda: calcular(nombre_empleado_entry.get(), nombre_empresa_entry.get(
), nombre_contacto_cliente_entry.get(), nombre_empresa_cliente_entry.get(), costo_producto_entry.get(), margen_estimado_entry.get()))
boton.place(x=370, y=160)


ventana.mainloop()
