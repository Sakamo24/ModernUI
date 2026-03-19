import flet as ft

class ModernTextField(ft.Container):
    def __init__(self, label="検索", prefix_icon=ft.Icons.SEARCH, on_change=None):
        super().__init__()
        
        self.width = float("inf")
        
        self.padding = 0
        
        self.margin = ft.margin.all(0)
        
        self.content = ft.TextField(
            label=label,
            on_change=on_change,
            expand=True,
            text_style=ft.TextStyle(color=ft.Colors.WHITE, size=18),
            label_style=ft.TextStyle(color=ft.Colors.WHITE54),
            filled=True,
            bgcolor=ft.Colors.GREY_900,
            border_radius=50, 
            prefix_icon=prefix_icon,
            border_color=ft.Colors.TRANSPARENT,
            focused_border_color=ft.Colors.BLUE,
            focused_border_width=2,
            content_padding=ft.padding.symmetric(vertical=12, horizontal=15),
        )

class SwitchTile(ft.Container):
    def __init__(self, label_text, default_value=True, on_change=None):
        super().__init__()
        # 横幅を最大に広げる
        self.width = float("inf") 
        
        # 中身の構築
        self.content = ft.Row(
            controls=[
                # 1. 左端の余白（ここを Container で作る）
                ft.Container(width=15), 
                
                # 2. ラベル（expand=True にすることで、スイッチを右端に押し出す）
                ft.Text(
                    label_text, 
                    color=ft.Colors.WHITE, 
                    size=16, 
                    expand=True  # これが重要！
                ),
                
                # 3. スイッチ（Flutter Toggles 準拠の色）
                ft.Switch(
                    value=default_value,
                    on_change=on_change,
                    active_color=ft.Colors.BLUE,
                    inactive_track_color=ft.Colors.GREY_400,
                    inactive_thumb_color=ft.Colors.GREY_700,
                ),
                
                # 4. 右端にも少し余白が欲しい場合は追加
                ft.Container(width=10),
            ],
        )


class ColorCircle:
    def __init__(self, color, on_select):
        self.color = color
        self.on_select = on_select
        self.container = None

    def show(self):
        self.check_icon = ft.Icon(ft.Icons.CHECK, color=ft.Colors.WHITE, size=20, visible=False)

        self.container = ft.Container(
            content=self.check_icon,
            width=45,
            height=45,
            bgcolor=self.color,
            border_radius=ft.BorderRadius.all(100),
            alignment=ft.Alignment.CENTER,
            border=ft.Border.all(2, ft.Colors.TRANSPARENT),
            on_click=lambda e: self.on_select(self),
        )
        return self.container

    def set_selected(self, is_selected, do_update=True):
        if is_selected:
            self.container.border = ft.Border.all(2, ft.Colors.WHITE)
            self.check_icon.visible = True
        else:
            self.container.border = ft.Border.all(2, ft.Colors.TRANSPARENT)
            self.check_icon.visible = False

        if do_update:
            try:
                self.container.update()
            except RuntimeError:
                pass


class ColorPaletteBox:
    def __init__(self, on_color_change):
        self.on_color_change = on_color_change
        self.circles = []

        self.all_colors = [
            ft.Colors.BLUE,
            ft.Colors.LIGHT_BLUE,
            ft.Colors.CYAN,
            ft.Colors.TEAL,
            ft.Colors.GREEN,
            ft.Colors.LIGHT_GREEN,
            ft.Colors.LIME,
            ft.Colors.YELLOW,
            ft.Colors.AMBER,
            ft.Colors.ORANGE,
            ft.Colors.DEEP_ORANGE,
            ft.Colors.RED,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.DEEP_PURPLE,
            ft.Colors.INDIGO,
            ft.Colors.BROWN,
            ft.Colors.BLUE_GREY,
        ]

    def handle_select(self, clicked_circle):
        for circle in self.circles:
            circle.set_selected(False)

        clicked_circle.set_selected(True)
        self.on_color_change(clicked_circle.color)

    def build(self):
        rows = []
        for i in range(0, 18, 6):
            line_colors = self.all_colors[i : i + 6]
            row_controls = []
            for c in line_colors:
                circle_instance = ColorCircle(c, self.handle_select)
                self.circles.append(circle_instance)
                row_controls.append(circle_instance.show())

            rows.append(ft.Row(controls=row_controls, alignment=ft.MainAxisAlignment.CENTER))

        if self.circles:
            self.circles[0].set_selected(True, do_update=False)

        return ft.Container(
            content=ft.Column(controls=rows, alignment=ft.MainAxisAlignment.SPACE_EVENLY, expand=True),
            width=380,
            height=220,
            bgcolor=ft.Colors.GREY_900,
            border_radius=ft.BorderRadius.all(20),
            alignment=ft.Alignment.CENTER,
            padding=10,
        )