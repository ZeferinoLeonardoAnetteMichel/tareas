import flet as ft

def LoginView(page: ft.Page):
    # --- Variables de control ---
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.PERSON,
        width=400,
        border_radius=10,
        border_color="purple",
        keyboard_type=ft.KeyboardType.EMAIL
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.KEY,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=10,
        border_color="purple"
    )

    mensaje = ft.Text("", color="red")

    # --- Funciones auxiliares ---
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def pantalla_principal():
        page.controls.clear()
        titulo_panel = ft.Container(
            content=ft.Text("Panel Principal", color="white", size=30, weight="bold"),
            bgcolor="purple",
            padding=20,
            width=600
        )
        
        menu = ft.Row(
            [
                ft.Column([ft.Icon(ft.Icons.HOME), ft.Text("Inicio")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column([ft.Icon(ft.Icons.SEARCH), ft.Text("Explorar")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column([ft.Icon(ft.Icons.PERSON), ft.Text("Perfil")], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            width=300
        )

        page.add(
            ft.Column(
                [
                    titulo_panel,
                    ft.Container(height=60),
                    ft.Text("Bienvenido al Sistema", size=40, weight="bold"),
                    ft.Text("Has iniciado sesión correctamente", size=20, color="grey"),
                    ft.Container(height=80),
                    menu
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    def login_click(e):
        # Lógica de validación
        if not correo.value or not contraseña.value:
            mensaje.value = "Por favor, llene todos los campos"
            mensaje.color = "red"
            page.update()
            return

        # Simulación de autenticación (manteniendo tu lógica)
        if correo.value == "admin@gmail.com" and contraseña.value == "1234":
            page.session.set("user", {"email": correo.value, "name": "Administrador"})
            mostrar_snackbar("¡Sesión iniciada correctamente!", ft.Colors.GREEN)
            pantalla_principal()
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    def go_to_registro(e):
        page.go("/registro")

    def go_to_forgot_password(e):
        page.go("/recuperar")

    # --- Definición de botones ---
    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesión",
        width=250,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_400,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    registro = ft.ElevatedButton(
        "Registrarme",
        width=200,
        on_click=go_to_registro,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_400,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    contraseña.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor=ft.Colors.PURPLE_200,
            color=ft.Colors.WHITE
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Inicio De Sesion", size=30, weight="bold", color="purple"),
                    ft.Container(height=10),
                    correo,
                    ft.Container(height=10),
                    contraseña,
                    ft.Container(height=10),
                    mensaje,
                    ft.Container(height=10),
                    ft.TextButton("¿Olvidaste tu contraseña?", on_click=go_to_forgot_password),
                    ft.Row([iniciar_sesion, registro], alignment=ft.MainAxisAlignment.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=15
            )
        ]
    )

def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.views.append(LoginView(page))
    page.update()

ft.app(target=main)