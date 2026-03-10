import flet as ft
from modernUI import ModernTextField, SwitchTile

def main(page: ft.Page):
    page.window.width = 380
    page.window.height = 800

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ModernTextField(prefix_icon=None))
    page.add(SwitchTile("ダークモード", default_value=True))


ft.run(main)
