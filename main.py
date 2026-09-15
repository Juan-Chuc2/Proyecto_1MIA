import flet as ft

#prueba de Interfaz
def main(page: ft.Page):

    page.title = "Configuración de Usuario"
    page.window.width = 900
    page.window.height = 600

    def settings(e):
        usuario = ft.TextField(label="Nombre de usuario")
        tema =  ft.Dropdown(label = "Tema", options=[ft.dropdown.Option("Claro"), ft.dropdown.Option("Oscuro")])
        idioma = ft.Dropdown(label="Idioma",options=[ft.dropdown.Option("es"),ft.dropdown.Option("es-ES"),ft.dropdown.Option("en"),ft.dropdown.Option("en-US")])
        fuente = ft.TextField(label="Tamaño de fuente",keyboard_type=ft.KeyboardType.NUMBER,)
        color_menu =ft.Button("Seleccionar color del menú")
        color_tema = ft.Button("Seleccionar color de letra")
        foto = ft.Button("Seleccionar foto")

        def guardar(e):
            print(usuario.value)
            print(tema.value)
            print(idioma.value)
            print(fuente.value)
            if tema.value == "Oscuro":
                page.theme_mode = ft.ThemeMode.DARK
            else:
                page.theme_mode = ft.ThemeMode.LIGHT

            if fuente.value:
                tamano = int(fuente.value)

                titulo.size = tamano
                subtitulo.size = tamano

            page.update()

        settings = ft.AlertDialog(
            title=ft.Text("Configuración de usuario"),
            content=ft.Column([usuario, tema, idioma, fuente, color_menu, color_tema, foto],),

            actions = [
                ft.Button("Guardar", on_click=guardar)
                ])

        page.show_dialog(settings)

    menu = ft.MenuBar(
        controls=[ft.SubmenuButton(content=ft.Text("Archivo"),controls=[ft.MenuItemButton(content=ft.Text("Nuevo"),),
        ft.MenuItemButton(content=ft.Text("Salir"),),],),

            ft.SubmenuButton(content=ft.Text("Edición"),controls=[ft.MenuItemButton(content=ft.Text("Copiar"),),ft.MenuItemButton(content=ft.Text("Pegar"),),],),

            ft.SubmenuButton(content=ft.Text("Ver"),controls=[ft.MenuItemButton(content=ft.Text("Vista"),),],),

            ft.SubmenuButton(content=ft.Text("Settings"),controls=[ft.MenuItemButton(content=ft.Text("Configuración"),on_click=settings,),],),])

    titulo = ft.Text("Mi aplicación", size=30)

    subtitulo = ft.Text("Gestión de configuración de usuario", size=18)
    page.add(menu,
             ft.Container(content=ft.Column([titulo, subtitulo], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                          alignment=ft.Alignment.CENTER, expand=True, ), )

ft.app(target=main)