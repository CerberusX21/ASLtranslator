import flet as ft
from text_display_panel import create_text_display
import time

def create_main_window(page: ft.Page):
    # Page configuration
    page.title = "ASL Translator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    page.bgColor = "#0f172a"

    is_translating = False
    word_mode = True

    top_left_img = ft.Image(
        src="assets/ok-.png",
        width=150,
        height=150,
        opacity= 0.8,
        top=5,
        left=10,
        fit=ft.ImageFit.CONTAIN,
        rotate=100
    )

    top_right_img = ft.Image(
        src="assets/yo-.png",
        width=200,
        height=200,
        opacity= 0.8,
        fit=ft.ImageFit.CONTAIN,
        top=10,
        right=10,
        rotate=200
    )

    bottom_left_img = ft.Image(
        src="assets/Peace-.png",
        width=150,
        height=150,
        opacity= 0.8,
        fit=ft.ImageFit.CONTAIN,
        bottom=5,
        left=10
    )

    title = ft.Container(
        content=ft.Column([
            ft.Text(
                "ASL TRANSLATOR",
                size=40,
                weight=ft.FontWeight.BOLD,
                color="white",
                text_align=ft.TextAlign.CENTER,
                width=page.width
            ),
            ft.Container(
                content=ft.Text(
                    "Sign Language to Text",
                    size=18,
                    color=ft.Colors.with_opacity(0.7, "white"),
                    text_align=ft.TextAlign.CENTER,
                ),
                alignment=ft.alignment.center,
            )
        ],
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=page.width,
        alignment=ft.alignment.center
    )

    mode_switch = ft.Row(
        [
            ft.Text("Letters", color="white"),
            ft.Switch(
                value=word_mode,
                on_change=lambda e: toggle_mode(e),
                active_color="#4CAF50",
                inactive_track_color="#F44336"
            ),
            ft.Text("Words", color="white"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    )

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
        bgcolor="#4CAF50",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            overlay_color=ft.Colors.with_opacity(0.2, "white"),
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
        bgcolor="#F44336",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            overlay_color=ft.Colors.with_opacity(0.2, "white"),
            animation_duration=300,
        ),
        width=150,
        visible=False
    )

    status_message = ft.Text(
        "Press START to begin detection",
        color=ft.Colors.with_opacity(0.7, "white"),
        italic=True
    )

    def toggle_mode(e):
        nonlocal word_mode
        word_mode = not word_mode
        if is_translating:
            update_output_text()
        page.update()

    def update_output_text():
        if word_mode:
            output.content.value = "Hello friend!"
        else:
            output.content.value = "A B C D"

    def start_translation(e):
        nonlocal is_translating
        is_translating = True
        start_button.visible = False
        stop_button.visible = True
        output.content.value = "Starting detection..."
        status_message.value = f"Detecting {'words' if word_mode else 'letters'}..."
        page.update()

        time.sleep(1)
        update_output_text()
        page.update()

    def stop_translation(e):
        nonlocal is_translating
        is_translating = False
        start_button.visible = True
        stop_button.visible = False
        output.content.value = "Ready for translation..."
        status_message.value = "Press START to begin detection"
        page.update()

    main_column = ft.Column(
        [
            title,
            mode_switch,
            ft.Container(height=20),
            output,
            ft.Container(height=20),
            ft.Row(
                [start_button, stop_button],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Container(height=10),
            status_message
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    main_container = ft.Container(
        content=main_column,
        padding=ft.padding.symmetric(horizontal=20),
        expand=True
    )

    return ft.Stack(
        [
            top_left_img,
            top_right_img,
            bottom_left_img,
            main_container
        ],
        expand=True
    )