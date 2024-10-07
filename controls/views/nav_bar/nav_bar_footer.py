import time
import flet as ft

from builder.app_manager import got_to_screen
from builder.app_manager  import GLOBAL_VAR

class botton_bar(ft.BottomAppBar):

    def __init__(self):
        super().__init__()
        self.bgcolor=ft.colors.TRANSPARENT
        # self.height = 200
        self.offset = (0,0.1)
    def build(self):
        self.content=ft.Container(
                        ink=False,
                        bgcolor="BLACK,0.8",
                        alignment=ft.alignment.center,
                        # width         = 150,
                        border_radius=ft.border_radius.all(32),
                        padding=0,
                        margin=0,
                        border= ft.border.all(4, "WHITE,0.02"),
                        blur=(18, 18),
                        content=ft.CupertinoSlidingSegmentedButton(
                            selected_index=2,
                            thumb_color="WHITE,0.06",
                            bgcolor="TRANSPARENT",
                            padding=ft.padding.symmetric(0, 10),

                            controls=[
                                    ft.Container(
                                        width=89,
                                        content= ft.Icon(name="arrow_back_ios_outlined"),
                                                    ),
                                    ft.Container(
                                        width=89,
                                        content= ft.Icon(name="HOME"),
                                        # on_click=lambda e: event_bottom_appbar(data='1')
                                                    ),
                                    ft.Container(
                                        width=89,
                                        content= ft.Icon(name="widgets_rounded"),

                                                    ),
                            ],
                            on_change=lambda e: self.event_bottom_appbar(data=e.data),
                        ),  # <=== NOTE COMA
            )

    def event_bottom_appbar(self,data): # ID: main_screen, event_Iconbutton
        # RESET DEFOUD FALSE SECOND SCREEN
        GLOBAL_VAR(set_global_var={
                                    'secundary_menu_show':False,
                                    # 'show_off':True,

                                    }

            )

        list_screen: dict = {
                    "0":"second_screen",
                    "1":"first_screen",
                    "2":"doc_screen",

        }
        current_screen = GLOBAL_VAR(get_global_var='current_screen')

        if data == "0":
            if not current_screen == "Please no exist input in database":
                got_to_screen(to_screen='second_screen' ,style='burble' ,time_style=0.8 )

        if data == "1":
            got_to_screen(to_screen='first_screen' ,style='burble' ,time_style=0.8 )

        time.sleep(0.3)

        GLOBAL_VAR(set_global_var={'show_off':True})
        self.content.content.selected_index=2
        self.content.update()
