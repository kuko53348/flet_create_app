import flet as ft

from builder.app_manager  import builder_app ,GLOBAL_VAR


# main_widget = GLOBAL_VAR(get_global_var="main_page")

def handle_dismissal(e):
    # main_widget.add(ft.Text("Drawer dismissed"))
    ...
def handle_change(e):
    # main_widget.add(ft.Text(f"Selected Index changed: {e.selected_index}"))
    # page.close(drawer)
    ...
nav_drawer = ft.NavigationDrawer(
        # elevation=18,
        elevation=24,
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        shadow_color="black",
        bgcolor = "surface,0.96",        #: ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
        surface_tint_color="black,0.4",
        indicator_color="grey,0.25",
        controls=[
            ft.Container(
                expand          = True,
                padding         = ft.padding.all(0),    #: padding.only(left=8, top=8, right=8, bottom=8),
                margin          = ft.margin.all(0),     #: margin.only (left=8, top=8, right=8, bottom=8),
                alignment       = ft.alignment.center,  #: top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right
                image_src       = f"bg_first_screen.jpeg",
                height        = 340,
                # offset        = (0,-0.05),
                # blur=(12,12),
                border_radius = ft.border_radius.only(top_left=16, top_right=18, bottom_left=48, bottom_right=100),               #: ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                border        = ft.border.all(4, ft.colors.SURFACE),       #: ft.border.only(Left=8, top=8, right=8, bottom=8),
                image_fit     = 'COVER',                                 #: CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                image_opacity = 0.80,
                #
                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),

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
                #: [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                expand          = True,
                ink             = False,                #: click effect ripple
                bgcolor         = "TRANSPARENT",        #: ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                padding         = ft.padding.all(8),    #: padding.only(left=8, top=8, right=8, bottom=8),
                margin          = ft.margin.all(8),     #: margin.only (left=8, top=8, right=8, bottom=8),
                alignment       = ft.alignment.center,  #: top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right
                content=ft.Text(
                            #: PROPERTY
                            value             = "Servicios Gastronomicos",
                            text_align        = ft.TextAlign.CENTER,
                            weight            = ft.FontWeight.BOLD,
                            # italic            = True,
                            size=18,
                            font_family       = "Consolas", #"Consolas ,RobotoSlab

            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
            ft.Divider(thickness=0.1),
            ft.NavigationDrawerDestination(
                label="Indroduccion",
                icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ACCOUNT_CIRCLE),
            ),
            ft.NavigationDrawerDestination(
                label="Documentacion",
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                label="Contactar",
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                selected_icon=ft.icons.PHONE,
            ),
            ft.NavigationDrawerDestination(
                label="Licence",
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )