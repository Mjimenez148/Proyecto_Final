import flet as ft
datos_empleados = {}

def VentanaPrincipal(page:ft.Page):
    page.title = "Ventana Principal"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    titulo= ft.Text("Registro de Personal")
    codigo = ft.TextField(label = 'Codigo empleado', autofocus=True)
    nombre =ft.TextField(label='Nombre')
    costo_hr_extra = ft.TextField(label = ' Costo por Hora extra')
    codigo_consulta = ft.TextField(label="Codigo de empleado")
    btHORAS = ft.TextButton("Ingreso Hrs Extra", on_click=lambda _:clickHrsEx(page))
    btReporte = ft.TextButton("Reporte de horas por empleado", on_click=lambda _:clickReporte(page))
    btEmpleado = ft.TextButton("Ingreso de empleado", on_click=lambda _:clickEmpleado(page))
    filaTitulo = ft.Row()
    filaBotones = ft.Row()
    filaTitulo.controls = [titulo]
    filaBotones.controls = [btEmpleado,btHORAS,btReporte]
    page.add(filaTitulo, filaBotones)

    def clickHrsEx(page:ft.Page):
      pass

    def clickReporte(page: ft.page):
       pass
    def clickEmpleado(page: ft.page):
       pass
ft.app(target = VentanaPrincipal)