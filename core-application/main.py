import flet as ft

latest_sign = "..."

def main(page: ft.Page):
    page.title = "ASL Translator"
    page.bgcolor = "#1e1e2f"
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    output = ft.Text(
        value=latest_sign,
        size=20,
        weight="bold",
        color="CYAN_200",
        text_align=ft.TextAlign.CENTER
    )

    def refresh_display(e):
        output.value = latest_sign
        page.update()

    # Outer card-like container
    card = ft.Container(
        content=ft.Column([
            ft.Text(
                "🤟 ASL → Text Translator",
                size=36,
                weight="bold",
                color="white"
            ),
            ft.Divider(height=20, color="transparent"),
            output,
            ft.ElevatedButton(
                "Refresh",
                on_click=refresh_display,
                bgcolor="BLUE_600",
                color="white",
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=40,
        border_radius=20,
        bgcolor="#2c2c44",
        shadow=ft.BoxShadow(
            spread_radius=3,
            blur_radius=15,
            color="BLACK45",
            offset=ft.Offset(4, 4)
        ),
        alignment=ft.alignment.center,
        width=500,
    )

    page.add(
        ft.Row(
            controls=[card],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main, view=ft.AppView.FLET_APP)
