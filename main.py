import flet as ft
import time

from controls.app_screen_db import GLOBAL_VAR
from controls.app_screen_manager import screens

from controls.views.nav_bar.nav_bar_footer import botton_bar
from controls.views.nav_bar.nav_app_bar import nav_app_bar ,nav_drawer_widget

from builder.builder_screens import screen_view


def check_plataforms(plataforms,main_page):
    OS_SYSTEM: dict = {
            # SMARTPHONES
            'ANDROID':{"width":680,"height":680},
            'IOS':{"width":680,"height":680},

            # OS
            'LINUX':{"width":760,"height":710},
            'MACOS':{"width":760,"height":710},
            'WINDOWS':{"width":760,"height":710}
            }


    data_db = OS_SYSTEM.get(plataforms)

    if plataforms == "LINUX" or plataforms == "MACOS" or plataforms == "WINDOWS":
        main_page.window.width=data_db.get('width')
        main_page.window.height=data_db.get('height')
        main_page.update()


def main(page: ft.Page):

    # page.window.title_bar_hidden = True
    # page.window.title_bar_buttons_hidden = True
    # page.window.focused = True
    # page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
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
    # CHECK SCREEN DEOENDIG PLATFORM
    check_plataforms(plataforms=page.platform.name ,main_page=page)

    # UPDATE MAIN SCREEN
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
