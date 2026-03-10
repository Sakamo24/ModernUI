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