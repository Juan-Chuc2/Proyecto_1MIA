import flet as ft
from flet_color_pickers import BlockPicker
import  guardado_logica
def main(page: ft.Page):

    page.title = "Configuración de Usuario"
    page.window.width = 900
    page.window.height = 600

    color_menu_valor = "#1a1d28"
    color_letra_valor = "#000000"
    foto_valor = ""

    file_picker = ft.FilePicker()
    page.services.append(file_picker)

    avatar = ft.CircleAvatar(foreground_image_src=foto_valor, radius=35)

    archivo = ft.Text("Archivo")
    nuevo = ft.Text("Nuevo")
    salir = ft.Text("Salir")
    edicion = ft.Text("Edición")
    copiar = ft.Text("Copiar")
    pegar = ft.Text("Pegar")
    ver = ft.Text("Ver")
    vista = ft.Text("Vista")
    settings = ft.Text("Settings")
    configuracion = ft.Text("Configuración")

    def aplicar_idioma(codigo):
        if codigo == "es":
            archivo.value = "Archivo"
            nuevo.value = "Nuevo"
            salir.value = "Salir"
            edicion.value = "Edición"
            copiar.value = "Copiar"
            pegar.value = "Pegar"
            ver.value = "Ver"
            vista.value = "Vista"
            settings.value = "Settings"
            configuracion.value = "Configuración"

        elif codigo == "es-ES":
            archivo.value = "Archivo"
            nuevo.value = "Nuevo"
            salir.value = "Salir"
            edicion.value = "Edición"
            copiar.value = "Copiar"
            pegar.value = "Pegar"
            ver.value = "Ver"
            vista.value = "Vista"
            settings.value = "Ajustes"
            configuracion.value = "Configuración"

        elif codigo == "en":
            archivo.value = "File"
            nuevo.value = "New"
            salir.value = "Exit"
            edicion.value = "Edit"
            copiar.value = "Copy"
            pegar.value = "Paste"
            ver.value = "View"
            vista.value = "View"
            settings.value = "Settings"
            configuracion.value = "Preferences"

        elif codigo == "en-US":
            archivo.value = "File"
            nuevo.value = "New"
            salir.value = "Quit"
            edicion.value = "Edit"
            copiar.value = "Copy"
            pegar.value = "Paste"
            ver.value = "View"
            vista.value = "View"
            settings.value = "Settings"
            configuracion.value = "Preferences"

        page.update()

    def abrir_settings(e):
        usuario = ft.TextField(label="Nombre de usuario")
        tema =  ft.Dropdown(label = "Tema", options=[ft.dropdown.Option("Claro"), ft.dropdown.Option("Oscuro")])
        idioma = ft.Dropdown(label="Idioma",options=[ft.dropdown.Option("es"),ft.dropdown.Option("es-ES"),ft.dropdown.Option("en"),ft.dropdown.Option("en-US")])
        fuente = ft.TextField(label="Tamaño de fuente",keyboard_type=ft.KeyboardType.NUMBER,)
        vista_previa = ft.Image(src=foto_valor if foto_valor else None, visible=bool(foto_valor), width=80,height=80,fit=ft.BoxFit.COVER,border_radius=ft.BorderRadius.all(40),)
        def elegir_color_menu(e):
            def cambiar(e):
                nonlocal color_menu_valor
                color_menu_valor = e.data
                page.update()
            picker = BlockPicker(color=color_menu_valor, on_color_change=cambiar)
            dialogo_color = ft.AlertDialog(title=ft.Text("Color de la barra de menú"),content=picker,actions=[ft.TextButton("Cerrar", on_click=lambda e: page.pop_dialog())],)
            page.show_dialog(dialogo_color)

        def elegir_color_letra(e):
            def cambiar(e):
                nonlocal color_letra_valor
                color_letra_valor = e.data
                page.update()
            picker = BlockPicker(color=color_letra_valor, on_color_change=cambiar)
            dialogo_color = ft.AlertDialog(title=ft.Text("Color de letra"),content=picker,actions=[ft.TextButton("Cerrar", on_click=lambda e: page.pop_dialog())],)
            page.show_dialog(dialogo_color)

        async def elegir_foto(e):
            nonlocal foto_valor
            archivos = await file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)
            if archivos:
                foto_valor = archivos[0].path
                vista_previa.src = foto_valor
                vista_previa.visible = True
                page.update()

        btn_color_menu =ft.Button("Seleccionar color del menú", on_click=elegir_color_menu)
        btn_color_letra = ft.Button("Seleccionar color de letra", on_click=elegir_color_letra)
        foto = ft.Button("Seleccionar foto", on_click=elegir_foto)

        def guardar(e):
            print(usuario.value)
            print(tema.value)
            print(idioma.value)
            print(fuente.value)

            datos = {
                "nombre_usuario": usuario.value,
                "tema_interfaz": tema.value,
                "idioma": idioma.value,
                "tamaño_fuente": int(fuente.value) if fuente.value else 13,
                "color_barra": color_menu_valor,
                "color_letra": color_letra_valor,
                "foto_perfil": foto_valor,
            }
            guardado_logica.guardar_configuracion(datos)

            if tema.value == "Oscuro":
                page.theme_mode = ft.ThemeMode.DARK
            else:
                page.theme_mode = ft.ThemeMode.LIGHT

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

            menu.style = ft.MenuStyle(bgcolor=color_menu_valor)

            titulo.color = color_letra_valor
            subtitulo.color = color_letra_valor
            archivo.color = color_letra_valor
            nuevo.color = color_letra_valor
            salir.color = color_letra_valor
            edicion.color = color_letra_valor
            copiar.color = color_letra_valor
            pegar.color = color_letra_valor
            ver.color = color_letra_valor
            vista.color = color_letra_valor
            settings.color = color_letra_valor
            configuracion.color = color_letra_valor

            avatar.foreground_image_src = foto_valor

            page.pop_dialog()
            page.update()

        dialogo_settings = ft.AlertDialog(
            title=ft.Text("Configuración de usuario"),
            content=ft.Column([usuario, tema, idioma, fuente, btn_color_menu, btn_color_letra, foto, vista_previa],),

            actions = [
                ft.Button("Guardar", on_click=guardar)
                ])

        page.show_dialog(dialogo_settings)

    menu = ft.MenuBar(
        controls=[ft.SubmenuButton(content=archivo,controls=[ft.MenuItemButton(content=nuevo,),
        ft.MenuItemButton(content=salir,),],),

            ft.SubmenuButton(content=edicion,controls=[ft.MenuItemButton(content=copiar,),ft.MenuItemButton(content=pegar,),],),

            ft.SubmenuButton(content=ver,controls=[ft.MenuItemButton(content=vista,),],),

            ft.SubmenuButton(content=settings,controls=[ft.MenuItemButton(content=configuracion,on_click=abrir_settings,),],)])

    titulo = ft.Text("Mi aplicación", size=30)

    subtitulo = ft.Text("Gestión de configuración de usuario", size=18)
    page.add(menu,
             ft.Container(content=ft.Column([avatar, titulo, subtitulo], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                          alignment=ft.Alignment.CENTER, expand=True, ), )

ft.run(main)