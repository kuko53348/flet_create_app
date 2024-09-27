import flet as ft

from builder.app_manager import got_to_screen
from builder.app_manager  import builder_app ,GLOBAL_VAR


def event_bottom_appbar(data): # ID: main_screen, event_Iconbutton
    # print(f"Demo App: {data} event_Iconbutton")
    list_screen: dict = {
                "0":"second_screen",
                "1":"first_screen",
                "2":"doc_screen",

    }
    current_screen = GLOBAL_VAR(get_global_var='current_screen')
    # print(current_screen)

    if data == "1":
        if not current_screen == 'first_screen':
            got_to_screen(to_screen=list_screen.get(data) ,style='burble' ,time_style=0.8 )
    if data == "0":
        if current_screen == 'doc_screen':
            got_to_screen(to_screen='second_screen' ,style='burble' ,time_style=0.8 )
        elif current_screen == 'second_screen':
            got_to_screen(to_screen='first_screen' ,style='burble' ,time_style=0.8 )

    bottom_appbar.content.content.selected_index=1
    bottom_appbar.update()
bottom_appbar = ft.BottomAppBar(
                                # height=72,
                                visible=False,
                                bgcolor=ft.colors.TRANSPARENT,
                                # shape=ft.NotchShape.CIRCULAR,
                                content=ft.Container(
                                            # expand          = True,
                                            ink=False,                #: click effect ripple
                                            bgcolor="BLACK,0.8",
                                            alignment=ft.alignment.center,
                                            width         = 150,
                                            border_radius=ft.border_radius.all(32),
                                            padding=0,
                                            margin=0,
                                            # shadow = ft.BoxShadow(
                                            #            spread_radius= 0,
                                            #            blur_radius  = 15,
                                            #            color        = ft.colors.CYAN,
                                            #            offset       = ft.Offset(0, 0),
                                            #            blur_style   = ft.ShadowBlurStyle.OUTER,
                                            #      ),
                                            blur=(18, 18),

                                            content=ft.CupertinoSlidingSegmentedButton(
                                                selected_index=1,
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
                                                            on_click=lambda e: event_bottom_appbar(data='1')
                                                                        ),
                                                        ft.Container(
                                                            width=89,
                                                            content= ft.Icon(name="ballot_outlined"),

                                                                        ),
                                                ],
                                                on_change=lambda e: event_bottom_appbar(data=e.data),
                                            ),  # <=== NOTE COMA
                                ))
