import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario_valido = "admin"
    password_valido = "12345"

    correo = ft.TextField(label="Correo electrónico", width=280, border_color="purple")

    contraseña = ft.TextField(
        label="Introduzca su contraseña",
        password=True,
        can_reveal_password=True,
        width=280,
        border_color="purple"
    )

    mensaje = ft.Text("")

    contenido = ft.Container()

    pagina_inicio = ft.Column(
        [
            ft.Text("Bienvenido al Sistema", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Has iniciado sesión correctamente")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_explorar = ft.Column(
        [
            ft.Icon(ft.Icons.EXPLORE, size=60),
            ft.Text("Explorar contenido", size=25)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    pagina_perfil = ft.Column(
        [
            ft.Icon(ft.Icons.PERSON, size=60),
            ft.Text("Perfil del usuario", size=25),
            ft.Text("admin@gmail.com")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    def cambiar_pagina(e):
        if e.control.selected_index == 0:
            contenido.content = pagina_inicio
        elif e.control.selected_index == 1:
            contenido.content = pagina_explorar
        elif e.control.selected_index == 2:
            contenido.content = pagina_perfil

        page.update()

    def login(e):

        if correo.value == "" or contraseña.value == "":
            mensaje.value = "Error: Debes llenar todos los campos"
            mensaje.color = "red"
            page.update()
            return

        if correo.value == usuario_valido and contraseña.value == password_valido:

            page.clean()

            contenido.content = pagina_inicio

            page.add(
                ft.Column(
                    [
                        contenido
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )

            page.navigation_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(
                        icon=ft.Icons.HOME,
                        label="Inicio"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.EXPLORE,
                        label="Explorar"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.PERSON,
                        label="Perfil"
                    ),
                ],
                on_change=cambiar_pagina
            )

            page.update()

        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    icono = ft.Icon(icon=ft.Icons.PERSON, size=60)

    sesion = ft.Container(
        width=350,
        padding=30,
        border_radius=10,
        bgcolor="grey200",
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Text("Iniciar sesión", size=40, weight="bold"),
                correo,
                contraseña,
                ft.ElevatedButton(
                    content=ft.Text("Iniciar sesión"),
                    width=280,
                    on_click=login
                ),
                mensaje,
                ft.TextButton(
                    content=ft.Text("¿Olvidaste tu contraseña?")
                    
                    
                )
            ]
        )
    )

    page.add(icono, sesion)

ft.app(target=main)