import flet as ft
from main_window import create_main_window

def main(page: ft.Page):
    page.title = "ASL Translator"
    page.bgColor = "#1e1e2f"
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    main_window = create_main_window(page)
    page.add(ft.Row(controls=[main_window], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main, view=ft.AppView.FLET_APP)