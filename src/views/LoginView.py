import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "Inicia sesión",
        size=30,
        weight="bold",
        color="purple"
    )

    usuario = ft.TextField(
    label="Usuario",
    width=300,
    border_color="purple",
    icon=ft.Icons.PERSON
)

    password = ft.TextField(
    label="Contraseña",
    password=True,
    can_reveal_password=True,
    width=300,
    border_color="purple",
    icon=ft.Icons.LOCK
)

    mensaje = ft.Text()

    def pantalla_principal():
        page.controls.clear()
        titulo_panel = ft.Container(
            content=ft.Text(
                "Panel Principal",
                color="white",
                size=30,
                weight="bold"
            ),
            bgcolor="purple",
            padding=20,
            width=600
        )

        bienvenido = ft.Text(
            "Bienvenido al Sistema",
            size=40,
            weight="bold"
        )

        subtexto = ft.Text(
            "Has iniciado sesión correctamente",
            size=20,
            color="grey"
        )
        menu = ft.Row(
            [
                ft.Column(
                    [
                        ft.Icon(ft.Icons.HOME),
                        ft.Text("Inicio")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Icon(ft.Icons.SEARCH),
                        ft.Text("Explorar")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Icon(ft.Icons.PERSON),
                        ft.Text("Perfil")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            width=300
        )

        page.add(
            ft.Column(
                [
                    titulo_panel,
                    ft.Container(height=60),
                    bienvenido,
                    subtexto,
                    ft.Container(height=80),
                    menu
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        page.update()

    def login(e):
        if usuario.value == "admin" and password.value == "1234":
            mensaje.value = "Bienvenido"
            mensaje.color = "green"
            page.update()
            pantalla_principal()
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    boton_login = ft.ElevatedButton(
        "Iniciar sesión",
        bgcolor="purple",
        color="white",
        on_click=login
    )

    page.add(
        ft.Column(
            [
                titulo,
                usuario,
                password,
                boton_login,
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

