import flet as ft
from controls.app_screen_db import GLOBAL_VAR
from builder import builder_screens
from controls.views.nav_bar.nav_app_bar import nav_app_bar

class got_to_screen():

    def __init__(self,
                to_screen= 'screen_name' ,
                style='ring' ,
                time_style=0.8,
                page = "",
                rotation: bool=False,
        ):
        super().__init__()
        # GET ROTATION MODULE ACCEPT
        self.rotation = rotation

        # GET BY DEFOULD MAIN SCREEN FIRST
        self.main_page = GLOBAL_VAR(get_global_var="main_page")
        self.main_page.on_route_chage=self.change_route(to_screen)
        self.main_page.update()

    def change_route(self,path):
        # THIS FUNC ONLY MAKE THAT APP SHOW LAST VIEW LIKE SELECTED VIEW BECOUSE
        # BY DEFOULD SHOW FIRST SCREEN LAST VIEW
        self.main_page.controls.clear()
        self.main_page.controls.append(GLOBAL_VAR(get_global_var=path))

        # ADD SPACE IN FOOTER
        # self.main_page.controls.append(ft.Container(height=300,bgcolor="red"))

        # SET VISIBLE APPBAR AND FOOTER BAR
        self.main_page.appbar.visible=True
        self.main_page.navigation_bar.visible=True

        if self.rotation:
            GLOBAL_VAR(set_global_var={'rotation': True})
        else:
            GLOBAL_VAR(set_global_var={'rotation': False})
