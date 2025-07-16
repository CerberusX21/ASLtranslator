import flet as ft
from text_display_panel import create_text_display
import time

def create_main_window(page: ft.Page):
    # Configuration de la page
    page.title = "🤟 ASL Translator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 30
    page.bgColor = "#0f172a"  # Fond bleu nuit

    # Variables d'état
    is_translating = False

    # Éléments UI
    title = ft.Text(
        "ASL TRANSLATOR",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER
    )

    subtitle = ft.Text(
        "Sign Language to Text",
        size=18,
        color=ft.Colors.with_opacity(0.7, "white"),
        text_align=ft.TextAlign.CENTER
    )

    # Zone de résultat avec effet spécial
    output = ft.Container(
        content=create_text_display("Ready for translation..."),
        padding=30,
        margin=ft.margin.symmetric(vertical=20),
        border_radius=15,
        bgcolor=ft.Colors.with_opacity(0.1, "white"),
        width=600,
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
        on_hover=lambda e: [
            setattr(e.control, "bgcolor",
                    ft.Colors.with_opacity(0.15, "white") if e.data == "true"
                    else ft.Colors.with_opacity(0.1, "white")),
            e.control.update()
        ]
    )

    start_button = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.PLAY_ARROW, color="white"),
                ft.Text("START", color="white"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        on_click=lambda e: start_translation(e),
        bgcolor="#4CAF50",  # Green
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            overlay_color=ft.Colors.with_opacity(0.2, "white"),
            elevation={"": 8, "pressed": 1},
            animation_duration=300,
        ),
        width=150,
    )

    stop_button = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.STOP, color="white"),
                ft.Text("STOP", color="white"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        on_click=lambda e: stop_translation(e),
        bgcolor="#F44336",  # Red
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            overlay_color=ft.Colors.with_opacity(0.2, "white"),
            elevation={"": 8, "pressed": 1},
            animation_duration=300,
        ),
        width=150,
        visible=False
    )

    # Status message at bottom
    status_message = ft.Text(
        "Press START to begin detection",
        color=ft.Colors.with_opacity(0.7, "white"),
        italic=True
    )

    def start_translation(e):
        nonlocal is_translating
        is_translating = True
        start_button.visible = False
        stop_button.visible = True
        output.content.value = "Starting detection..."
        status_message.value = "Detection in progress..."
        page.update()

        # Simulate translation process
        time.sleep(1)
        output.content.value = "👋 Hello! How are you?"
        page.update()

    def stop_translation(e):
        nonlocal is_translating
        is_translating = False
        start_button.visible = True
        stop_button.visible = False
        output.content.value = "Ready for translation..."
        status_message.value = "Press START to begin detection"
        page.update()

    # Main layout
    main_column = ft.Column(
        [
            ft.Divider(height=20),
            title,
            subtitle,
            ft.Divider(height=40),
            output,
            ft.Divider(height=30),
            ft.Row(
                [start_button, stop_button],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Divider(height=30),
            status_message
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    return ft.Container(
        content=main_column,
        padding=ft.padding.symmetric(horizontal=20),
        expand=True
    )