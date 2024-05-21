import flet as ft
datos_empleados = {}

def VentanaPrincipal(page:ft.Page):
    page.title = "Ventana Principal"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    titulo= ft.Text("Registro de Personal")
    mensajes= ft.Text("Area de mensajes")
    codigo = ft.TextField(label = 'Codigo empleado', autofocus=True)
    nombre =ft.TextField(label='Nombre')
    costo_hr_extra = ft.TextField(label = ' Costo por Hora extra')
    codigo_consulta = ft.TextField(label="Codigo de empleado")
    btHORAS = ft.TextButton("Ingreso Hrs Extra", on_click=lambda _:clickHrsEx(page))
    btReporte = ft.TextButton("Reporte de horas por empleado", on_click=lambda _:clickReporte(page))
    btEmpleado = ft.TextButton("Ingreso de empleado", on_click=lambda _:clickEmpleado(page))
    filaTitulo = ft.Row()
    filaBotones = ft.Row()
    colFormulario = ft.Column()
    filaContenido = ft.Row()
    filaTitulo.controls = [titulo]
    filaBotones.controls = [btEmpleado,btHORAS,btReporte]
    page.add(filaTitulo, filaBotones)

    def clickHrsEx(page:ft.Page):
      pass

    def clickReporte(page: ft.page):
       pass
    def clickEmpleado(page: ft.page):
       filaBotones2 = ft.Row()
       btnGuardar = ft.ElevatedButton("Guardar", on_click=lambda _:guardar(page))
       btnCancelar = ft.ElevatedButton("Cancelar", on_click=lambda _:borrarCampos())
       filaBotones2.controls = [btnGuardar, btnCancelar]
       colFormulario.controls = [codigo, nombre, costo_hr_extra]
       filaContenido.controls = [colFormulario]
       mensajes.value='Ingreso de datos Nuevo Empleado'
       borrarCampos()
       page.update()
       

    def guardar(page: ft.page):
       pass

    def borrarCampos():
       pass
ft.app(target = VentanaPrincipal)