import flet as ft
from modernUI import ColorPaletteBox

def main(page: ft.Page):
    # 最新版の書き方（あなたが最初に書いた通りです！）
    page.window.width = 380
    page.window.height = 800

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ここだけ「色を変えて画面を更新する」処理を追加しました
    def on_change(e):
        if e.control.bgcolor == ft.Colors.GREY_900:
            e.control.bgcolor = ft.Colors.BLUE
        else:
            e.control.bgcolor = ft.Colors.GREY_900
        e.control.update()

    con = ft.Container(
        bgcolor=ft.Colors.GREY_900,
        width=300,
        height=300,
        border_radius=20,
        on_click=on_change,
        alignment=ft.Alignment.CENTER,  # ← あなたが書いた大文字が正解です
        content=ft.Text("ここをクリック！", color=ft.Colors.WHITE, size=20)
    )

    a = ColorPaletteBox(on_color_change=lambda c: print(f"Selected color: {c}"))

    page.add(con, a.build())

# 起動コマンドも最新版の書き方です
ft.run(main)