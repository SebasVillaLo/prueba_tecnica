import tkinter


def validador_entero(entero):
    try:
        if entero == '':
            entero = 0
        int(entero)
        return int(entero)
    except ValueError:
        return tkinter.messagebox.showinfo("Error", "Revisa los campos donde pide un numero entero!")


def calcular(nombre_empleado_entry, nombre_empresa_entry, nombre_contacto_cliente_entry, nombre_empresa_cliente_entry, costo_producto_entry, margen_estimado_entry):
    # Creamos las variables para almacenar los datos ingresados
    variables_principales = {'nombre_empleado': nombre_empleado_entry,
                             'nombre_empresa': nombre_empresa_entry,
                             'nombre_contacto_cliente': nombre_contacto_cliente_entry,
                             'nombre_empresa_cliente': nombre_empresa_cliente_entry,
                             'costo_producto': validador_entero(costo_producto_entry),
                             'margen_estimado': validador_entero(margen_estimado_entry)}

    mensajes_error = {
        'nombre_empleado': "Nombre del empleado",
        'nombre_empresa': "Nombre de la empresa",
        'nombre_contacto_cliente': "Nombre del contacto del cliente",
        'nombre_empresa_cliente': "Nombre de la empresa del cliente",
        'costo_producto': "Costo del producto",
        'margen_estimado': "Margen estimado"
    }
    inputs_vacios_list = []

    for key, value in variables_principales.items():
        if not value or value == "":
            inputs_vacios_list.append(mensajes_error[key])

    if len(inputs_vacios_list) > 0:
        tkinter.messagebox.showinfo("Error", "No pudimos procesar el precio ya que no tenemos el {}!".format(
            ', '.join(inputs_vacios_list)))
    #  Resultado debe darle a precio de venta
    else:
        resultado = variables_principales['costo_producto'] / \
            (1 - variables_principales['margen_estimado'] / 100)
        tkinter.messagebox.showinfo("Resultado", '''
    Hola {}!\n
    El precio de venta del producto que deseas
    entregar a {} de la
    compañía {} es de ${:0,.2f}.\n
    Con esta venta la {} tendrá
    una utilidad de ${:0,.2f}.
        '''.format(variables_principales['nombre_empleado'], variables_principales['nombre_contacto_cliente'], variables_principales['nombre_empresa_cliente'], int(resultado), variables_principales['nombre_empresa'], int(resultado - variables_principales['costo_producto'])))