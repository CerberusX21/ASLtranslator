import flet as ft

def create_text_display(initial_text="..."):
    return ft.Text(
        value=initial_text,
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#00e5ff",
        text_align=ft.TextAlign.CENTER,
        selectable=True,
    )