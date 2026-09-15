import flet as ft

def main(page: ft.Page):

    page.title = "Configuración de Usuario"
    page.window.width = 900
    page.window.height = 600

    txt_archivo = ft.Text("Archivo")
    txt_nuevo = ft.Text("Nuevo")
    txt_salir = ft.Text("Salir")
    txt_edicion = ft.Text("Edición")
    txt_copiar = ft.Text("Copiar")
    txt_pegar = ft.Text("Pegar")
    txt_ver = ft.Text("Ver")
    txt_vista = ft.Text("Vista")
    txt_settings = ft.Text("Settings")
    txt_configuracion = ft.Text("Configuración")

    def aplicar_idioma(codigo):
        if codigo == "es":
            txt_archivo.value = "Archivo"
            txt_nuevo.value = "Nuevo"
            txt_salir.value = "Salir"
            txt_edicion.value = "Edición"
            txt_copiar.value = "Copiar"
            txt_pegar.value = "Pegar"
            txt_ver.value = "Ver"
            txt_vista.value = "Vista"
            txt_settings.value = "Settings"
            txt_configuracion.value = "Configuración"

        elif codigo == "es-ES":
            txt_archivo.value = "Archivo"
            txt_nuevo.value = "Nuevo"
            txt_salir.value = "Salir"
            txt_edicion.value = "Edición"
            txt_copiar.value = "Copiar"
            txt_pegar.value = "Pegar"
            txt_ver.value = "Ver"
            txt_vista.value = "Vista"
            txt_settings.value = "Ajustes"
            txt_configuracion.value = "Configuración"

        elif codigo == "en":
            txt_archivo.value = "File"
            txt_nuevo.value = "New"
            txt_salir.value = "Exit"
            txt_edicion.value = "Edit"
            txt_copiar.value = "Copy"
            txt_pegar.value = "Paste"
            txt_ver.value = "View"
            txt_vista.value = "View"
            txt_settings.value = "Settings"
            txt_configuracion.value = "Preferences"

        elif codigo == "en-US":
            txt_archivo.value = "File"
            txt_nuevo.value = "New"
            txt_salir.value = "Quit"
            txt_edicion.value = "Edit"
            txt_copiar.value = "Copy"
            txt_pegar.value = "Paste"
            txt_ver.value = "View"
            txt_vista.value = "View"
            txt_settings.value = "Settings"
            txt_configuracion.value = "Preferences"

        page.update()

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

            if idioma.value:
                aplicar_idioma(idioma.value)

            page.pop_dialog()
            page.update()

        settings = ft.AlertDialog(
            title=ft.Text("Configuración de usuario"),
            content=ft.Column([usuario, tema, idioma, fuente, color_menu, color_tema, foto],),

            actions = [
                ft.Button("Guardar", on_click=guardar)
                ])

        page.show_dialog(settings)

    menu = ft.MenuBar(
        controls=[ft.SubmenuButton(content=txt_archivo,controls=[ft.MenuItemButton(content=txt_nuevo,),
        ft.MenuItemButton(content=txt_salir,),],),

            ft.SubmenuButton(content=txt_edicion,controls=[ft.MenuItemButton(content=txt_copiar,),ft.MenuItemButton(content=txt_pegar,),],),

            ft.SubmenuButton(content=txt_ver,controls=[ft.MenuItemButton(content=txt_vista,),],),

            ft.SubmenuButton(content=txt_settings,controls=[ft.MenuItemButton(content=txt_configuracion,on_click=settings,),],),])

    titulo = ft.Text("Mi aplicación", size=30)

    subtitulo = ft.Text("Gestión de configuración de usuario", size=18)
    page.add(menu,
             ft.Container(content=ft.Column([titulo, subtitulo], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                          alignment=ft.Alignment.CENTER, expand=True, ), )

ft.run(main)