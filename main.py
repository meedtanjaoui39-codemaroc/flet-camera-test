import flet as ft
import flet_camera as fc


async def main(page: ft.Page):
    page.title = "Camera Test"

    camera = fc.Camera(
        expand=True,
        preview_enabled=True,
    )

    cameras = await camera.get_available_cameras()

    if cameras:
        await camera.initialize(
            description=cameras[0],
            resolution_preset=fc.ResolutionPreset.MEDIUM,
            enable_audio=False,
        )

    page.add(camera)


ft.run(main)
