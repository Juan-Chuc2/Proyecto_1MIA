import flet as ft
from flet_color_pickers import BlockPicker
import guardado_proyecto as guardado

def main(page: ft.Page):

    page.title = "Configuración de Usuario"
    page.window.width = 900
    page.window.height = 600

    color_menu_valor = "#1a1d28"
    color_letra_valor = "#000000"
    foto_valor = ""
    nombre_usuario_valor = "usuario"
    tema_valor = "claro"
    idioma_valor = "es"
    fuente_valor = 13

    file_picker = ft.FilePicker()
    page.services.append(file_picker)

    aviso = ft.SnackBar(content=ft.Text(""))
    page.services.append(aviso)

    def mostrar_aviso(mensaje):
        aviso.content = ft.Text(mensaje)
        aviso.open = True
        page.update()

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

    titulo = ft.Text(nombre_usuario_valor, size=30)
    subtitulo = ft.Text("Gestión de configuración de usuario", size=18)

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
            subtitulo.value = "Gestión de configuración de usuario"

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
            subtitulo.value = "Gestión de configuración de usuario"

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
            subtitulo.value = "User configuration management"

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
            subtitulo.value = "User settings management"

    def aplicar_configuracion(config):
        nonlocal color_menu_valor, color_letra_valor, foto_valor
        nonlocal nombre_usuario_valor, tema_valor, idioma_valor, fuente_valor

        nombre_usuario_valor = config["nombre_usuario"]
        tema_valor = config["tema_interfaz"]
        idioma_valor = config["idioma"]
        fuente_valor = config["tamaño_fuente"]
        color_menu_valor = config["color_barra"]
        color_letra_valor = config["color_letra"]
        foto_valor = config["foto_perfil"]

        aplicar_idioma(idioma_valor)

        titulo.value = nombre_usuario_valor

        if tema_valor == "oscuro":
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        titulo.size = fuente_valor
        subtitulo.size = fuente_valor

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

        page.update()

    def abrir_settings(e):
        usuario = ft.TextField(label="Nombre de usuario", value=nombre_usuario_valor)
        tema =  ft.Dropdown(label = "Tema", value=tema_valor.capitalize(), options=[ft.dropdown.Option("Claro"), ft.dropdown.Option("Oscuro")])
        idioma = ft.Dropdown(label="Idioma", value=idioma_valor, options=[ft.dropdown.Option("es"),ft.dropdown.Option("es-ES"),ft.dropdown.Option("en"),ft.dropdown.Option("en-US")])
        fuente = ft.TextField(label="Tamaño de fuente",keyboard_type=ft.KeyboardType.NUMBER, value=str(fuente_valor),)
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
                "tema_interfaz": tema.value.lower(),
                "idioma": idioma.value,
                "tamaño_fuente": int(fuente.value) if fuente.value else 13,
                "color_barra": color_menu_valor,
                "color_letra": color_letra_valor,
                "foto_perfil": foto_valor,
            }

            exito, mensaje = guardado.guardar_configuracion(datos)
            aplicar_configuracion(datos)

            page.pop_dialog()
            page.update()
            mostrar_aviso(mensaje)

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

    page.add(menu,
             ft.Container(content=ft.Column([avatar, titulo, subtitulo], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                          alignment=ft.Alignment.CENTER, expand=True, ), )

    async def cargar_existente(e):
        page.pop_dialog()

        archivos = await file_picker.pick_files(
            dialog_title="Seleccioná tu archivo de configuración",
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["json"],
            allow_multiple=False,
        )

        if not archivos:
            mostrar_aviso("No se seleccionó ningún archivo, se usan valores por defecto.")
            datos = guardado.Config_por_defecto.copy()
            aplicar_configuracion(datos)
            return

        datos, mensaje, estado = guardado.cargar_configuracion(archivos[0].path)

        if estado in ("corrupto", "formato_invalido", "sin_permisos"):
            mostrar_error_carga(mensaje, datos)
        else:
            aplicar_configuracion(datos)
            mostrar_aviso(mensaje)

    def mostrar_error_carga(mensaje, datos_por_defecto):
        def usar_defecto(e):
            page.pop_dialog()
            aplicar_configuracion(datos_por_defecto)
            mostrar_aviso("Se cargaron los valores por defecto.")

        def cancelar(e):
            page.pop_dialog()
            page.show_dialog(dialogo_inicio)

        dialogo_error = ft.AlertDialog(
            modal=True,
            title=ft.Text("No se pudo cargar el archivo"),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton("Cancelar", on_click=cancelar),
                ft.Button("Usar valores por defecto", on_click=usar_defecto),
            ],
        )
        page.show_dialog(dialogo_error)

    def generar_nueva(e):
        datos = guardado.Config_por_defecto.copy()
        exito, mensaje = guardado.guardar_configuracion(datos)
        aplicar_configuracion(datos)
        page.pop_dialog()
        mostrar_aviso(mensaje)

    dialogo_inicio = ft.AlertDialog(
        modal=True,
        title=ft.Text("Bienvenido"),
        content=ft.Text("¿Querés cargar tu configuración guardada o generar una nueva?"),
        actions=[
            ft.TextButton("Cargar configuración guardada", on_click=cargar_existente),
            ft.Button("Generar nueva configuración", on_click=generar_nueva),
            ])

    page.show_dialog(dialogo_inicio)

ft.run(main)