import flet as ft


def main(page: ft.Page):
    page.title = "Camera Test"

    camera = ft.Camera()

    page.add(camera)


ft.run(main)
