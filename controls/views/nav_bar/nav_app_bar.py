import flet as ft
from ..keys_all_data_db import my_doc

class nav_drawer_widget(ft.NavigationDrawer):
    # globalVar='Erase this test'
    dict_documentation: dict={
        "0":"Introduccion",
        "1":"Agradecimientos",
        "2":"Documentacion",
        "3":"Desarrollador",
        "4":"Open Source License",

        }
    def __init__(self,main_page: dict):
        super().__init__()
        self.page = main_page

        self.shadow_color="black"
        self.elevation=24
        self.bgcolor = "surface,0.96",
        self.surface_tint_color="black,0.4"
        self.indicator_color="grey,0.25"

    def build(self):
        self.controls=[
                    ft.Container(
                        padding       = ft.padding.all(0),
                        margin        = ft.margin.all(0),
                        # expand        = True,
                        alignment     = ft.alignment.center,
                        height        = 340,
                        border_radius = ft.border_radius.only(top_left=16, top_right=18, bottom_left=48, bottom_right=100),
                        border        = ft.border.all(4, ft.colors.SURFACE),
                        content= ft.Image(
                                        src="bg_first_screen.jpeg",
                                        fit=ft.ImageFit.COVER,
                                        opacity=0.80,
                                        expand          = True,
                                        scale           = 1.2,
                                        ),
                        shadow = ft.BoxShadow(
                                   spread_radius= 1,
                                   blur_radius  = 22,
                                   color        = ft.colors.BLACK,
                                   offset       = ft.Offset(0, 0),
                                   blur_style   = ft.ShadowBlurStyle.OUTER,
                             ),
                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                    ft.Divider(thickness=0.1),
                    ft.Container(

                        expand          = True,
                        ink             = False,
                        bgcolor         = "TRANSPARENT",
                        padding         = ft.padding.all(8),
                        margin          = ft.margin.all(8),
                        alignment       = ft.alignment.center,
                        content=ft.Text(
                                    value             = "Servicios Gastronómicos",
                                    text_align        = ft.TextAlign.CENTER,
                                    weight            = ft.FontWeight.BOLD,
                                    # italic            = True,
                                    size=18,
                                    font_family       = "Consolas", #"Consolas ,RobotoSlab

                    ),),
                    ft.Divider(thickness=0.1),
                    ft.NavigationDrawerDestination(
                        label="Introducción",
                        icon_content=ft.Icon(ft.icons.EMOJI_FOOD_BEVERAGE_OUTLINED),
                        selected_icon=ft.icons.EMOJI_FOOD_BEVERAGE,
                    ),
                    ft.NavigationDrawerDestination(
                        label="Agradecimientos",
                        icon_content=ft.Icon(ft.icons.HANDSHAKE_OUTLINED,),
                        selected_icon=ft.icons.HANDSHAKE,
                    ),
                    ft.NavigationDrawerDestination(
                        label="Documentación",
                        icon=ft.icons.AUTO_STORIES_OUTLINED,
                        selected_icon_content=ft.Icon(ft.icons.AUTO_STORIES),
                    ),
                    ft.NavigationDrawerDestination(
                        label="Desarrollador",
                        icon_content=ft.Icon(ft.icons.CLEAN_HANDS_OUTLINED),
                        selected_icon=ft.icons.CLEAN_HANDS,
                    ),
                    ft.NavigationDrawerDestination(
                        label="Open Source Licence",
                        icon_content=ft.Icon(ft.icons.LOCAL_MALL_OUTLINED),
                        selected_icon=ft.icons.LOCAL_MALL,
                    ),
        ]
        self.on_change=lambda e:self.handle_change(index_data=e)

    def handle_change(self,index_data):
        # MODEL OF DATA SELECTED
        self.all_index_database = my_doc
        self.tmp_index_data = index_data.data
        self.model_data = self.dict_documentation.get(self.tmp_index_data)

        dlg_modal = ft.AlertDialog(
                                title=ft.Text(self.model_data),
                                # adaptive=True,
                                modal=True,
                                inset_padding = ft.padding.symmetric(vertical=12, horizontal=8),
                                content=ft.Column(
                                    scroll="HIDDEN",
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,

                                    controls=[ft.Text(
                                                    size=12,
                                                    value=self.all_index_database(arg=self.model_data),
                                                    text_align=ft.TextAlign.LEFT,
                                                    ),],),
                                actions=[
                                    ft.ElevatedButton(
                                                text="Cerrar",
                                                bgcolor='red',
                                                on_click=lambda _:self.page.close(dlg_modal),
                                                ),
                                ],
                                actions_alignment=ft.MainAxisAlignment.END,
        )


        self.page.open(dlg_modal)

class nav_app_bar(ft.AppBar):

    def __init__(self,main_page):
        super().__init__()
        self.page = main_page
        self.title=ft.Text(value="Restauración",)
        self.leading=ft.Icon(name=ft.icons.COFFEE_ROUNDED,)
        self.center_title=False
        self.actions=[ft.IconButton(icon=ft.icons.TABLE_ROWS_ROUNDED,on_click=lambda e: self.check_menu_bar(main_page=self.page)),]
        self.bgcolor ="TRANSPARENT"
        self.page.update()

    def check_menu_bar(self,main_page):
        main_page.open(main_page.drawer)