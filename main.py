import flet as ft
from builder.app_manager  import builder_app ,GLOBAL_VAR

# from controls.app_style_manager import styles
from controls.app_screen_manager import screens
from controls.views.nav_bar.nav_bar import  bottom_appbar
from controls.views.nav_bar.nav_drawer import  NavDrawerWidget

def change_size(page_width: float, page_height: float):
    #: RESIZE HEIGHT FROM SCREEN
    all_screens:    dict = GLOBAL_VAR(get_global_var='all_screens')
    current_screen: dict = GLOBAL_VAR(get_global_var='current_screen')

    #: UPDATE SIZE STREAMINGE
    data = all_screens.get(current_screen)
    data.height , data.width  = page_height , page_width
    data.update()

def check_menu_bar(main_page):
    current_screen: dict = GLOBAL_VAR(get_global_var='current_screen')
    if not current_screen == "main_screen":
        main_page.open(main_page.drawer)


def main(page: ft.Page):
    # GLOBAL_VAR(set_global_var={'main_page': page})

    # page.scroll               = "HIDDEN"              #: AUTO ADAPTIVE ALWAYS HIDDEN
    page.vertical_alignment   = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #:  COLOR
    page.theme_mode           = ft.ThemeMode.DARK
    # page.bgcolor              = ft.colors.BLACK
    # page.window_bgcolor       = ft.colors.TRANSPARENT

    #: POSITION OF SCREENS
    page.window.left          = 0
    page.window.top           = 0
    # page.window_center()

    #:======================== production RESIZE
    # page.window.height        = 350  # 566 620 710
    # page.window.width         = 710  # 295 320 350

    # page.window.height        = 710  # 566 620 710
    # page.window.width         = 350  # 295 320 350
    #=================================================
    page.window.height        = 768   # 295 320 350
    page.window.width         = 960  # 295 320 350

    page.padding              = 0
    page.spacing              = 0
    page.expand               = True

    #: SCREEN BUILDER
    tmp_screens = builder_app(screen=screens, main_page=page ) #: it's necessary to call all screens
    # all_screens = tmp_screens.get('show_all_screens')                           #: return one dict with all  screens inside
    show_screen = tmp_screens.get('builder_app')                                #: return exactly first screen

    #: UPDATE SIZE OF MAIN PHGONE SCREEN
    show_screen.height = page.window.height
    show_screen.width  = page.window.width
    page.on_resized    = lambda _: change_size(page_width=page.window.width, page_height=page.window.height)

    #: WALLPAPER
    # page.decoration   = ft.BoxDecoration(image=ft.DecorationImage(src="exemple.jpg",fit=ft.ImageFit.COVER,opacity=0.2,), #: CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
    #                    # gradient = ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
    #                    # gradient = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
    #                                )

    #: SET FROM CONTAINER BGCOLOR
    # page.bgcolor = styles['_2921']['bgcolor']
    # styles['_2921']['bgcolor'] ="red"

    # print(styles.get('_2921').get('bgcolor'))
    #: WE SET HOT SCOPE VAR
    # trailing=ft.Icon(ft.icons.WB_SUNNY_OUTLINED),
    current_screen: dict = GLOBAL_VAR(get_global_var='current_screen')
    # page.appbar = ft.AppBar(
    #                         title=ft.Text(value="Restauracion",),
    #                         leading=ft.Icon(name=ft.icons.COFFEE_ROUNDED,),
    #                         center_title=False,
    #                         actions=[ft.IconButton(icon=ft.icons.TABLE_ROWS_ROUNDED,on_click=lambda e: check_menu_bar(main_page=page)),],
    #                         )
    #  NAV DRAWER APP VAR
    # print(dir(page))
    # if current_screen == "first_screen":
    page.appbar = ft.AppBar(
                            visible=False,
                            title=ft.Text(value="Restauración",),
                            leading=ft.Icon(name=ft.icons.COFFEE_ROUNDED,),
                            center_title=False,
                            actions=[ft.IconButton(icon=ft.icons.TABLE_ROWS_ROUNDED,on_click=lambda e: check_menu_bar(main_page=page)),],
                            )
    page.drawer=NavDrawerWidget(main_widget=page)

    #  NAV APP VAR
    page.bottom_appbar = bottom_appbar

    page.add(show_screen)
    page.update()
    # page.open(page.drawer)

    # styles['_2921']['bgcolor'] ="Cyan"

def run_app():
    """
    - NO ERASE THIS FUNCTION
    - ONLY RUN CREATING PYPY PACKAGE
    """
    ft.app(
            target=main,
            )

if __name__ == '__main__':
    # import warnings
    # warnings.simplefilter('ignore',DeprecationWarning)

    ft.app(
            target=main,
            assets_dir="assets",
            # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            # web_renderer = ft.WebRenderer.HTML,
            # port=21109,
            )
