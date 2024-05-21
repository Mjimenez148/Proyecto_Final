import flet as ft
datos_empleados = {}

def VentanaPrincipal(page:ft.Page):
    page.title = "Ventana Principal"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    titulo= ft.TextField("Registro de Personal")
    codigo = ft.TextField(label = 'Codigo empleado')
    nombre =ft.TextField(label='Nombre')
    costo_hr_extra = ft.TextField(label = ' Costo por Hora extra')
    btHORAS = ft.TextButton("Ingreso Hrs Extra", on_click=lambda _:clickHrsEx(page))
    btReporte = ft.TextButton("Reporte de horas por empleado", on_click=lambda _:clickReporte(page))
    filatitulo = ft.row()
    filabotones = ft.row()
    filatitulo.controls = [titulo]
    filabotones.controls = [btHORAS,btReporte]
    page.add(filabotones, filatitulo)

    def clickHrsEx(page:ft.Page):
      pass

    def clickReporte(page: ft.page):
       pass

ft.app(target = VentanaPrincipal)