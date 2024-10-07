import flet as ft
import time

from controls.app_screen_db import GLOBAL_VAR
from controls.app_screen_manager import screens

from controls.views.nav_bar.nav_bar_footer import botton_bar
from controls.views.nav_bar.nav_app_bar import nav_app_bar ,nav_drawer_widget

from builder.builder_screens import screen_view

def main(page: ft.Page):
    # page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
    page.vertical_alignment        = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
    #:  COLOR
    page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
    #: POSITION OF SC
    # page.window.left               = 0
    # page.window.top                = 0
    # page.window_center()
    #
    #: SIZE
    # page.window.height             = 0
    # page.window.width              = 0
    page.padding                   = 0
    # page.margin                    = 0
    # page.spacing                   = 0
    page.expand                    = True

    # UP BAR
    page.appbar = nav_app_bar(main_page=page)
    page.drawer = nav_drawer_widget(main_page=page)
    page.appbar.visible=False
    # FOOTER BAR
    page.navigation_bar = botton_bar()
    page.navigation_bar.visible=False

    page.controls.append(
                        screen_view(
                            page=page,
                            content=screens.get("main_screen")
                            )
                        )
    page.update()
    # NECESSARY
    GLOBAL_VAR(set_global_var={"main_page":page})
    GLOBAL_VAR(set_global_var=screens)
    # print(page.window.height)
    # print(page.window.width)
if __name__ == '__main__':
    ft.app(
            assets_dir = "assets",
            target       = main,
            # port         = 8080,
            # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            # web_renderer = ft.WebRenderer.HTML

            )