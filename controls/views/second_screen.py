#: MAIN WIDGET SCREEN CLASS
import flet as ft
from ..app_screen_db import GLOBAL_VAR

from .second_screen_styles import styles
from .second_screen_events import *
from .keys_db import index_database

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "height": "625",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        "width": "460",
        "image": {
                'src':"image_menu.jpeg",
                "opacity": "0.21999999999999997",
                "fit": "cover"
                },
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "blur": {"sigma_x":20,"sigma_y":20,"tile_mode":"mirror"},
        "padding": {"l":0,"t":0,"r":0,"b":0}
    },
    "COLUMN_CONTAINER": {
        "alignment": "center",
        "scroll": "",
        "spacing": "2",
        "tight": "false",
        "horizontal_alignment": "center"
    }
}

class second_screen(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.second_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):

        #  CONTAINER THAT HAVE SECONDARY MENU TO GO TO DOC PAGE

        self.show_secundary_menu = ft.Container(  # Container_Column
                                        **self.dict_style('_4155'),
                                        visible=False,

                                        content=ft.Column(  # Column
                                            **self.dict_style('_4156'),
                                            controls=[],
                                            ),)  # // LAYER 1 END

        self.add_menu = ft.Column( # Column
                    **self.dict_style('_4140'),
                    controls= [
                                #====================
                                # self.builder_main_menu,
                                ],)

        #: MAIN PHONE CONTAINER
        self.content_box = [
                    ft.Container(  # Container_Stack
                        **self.dict_style('_4131'),
                        content= ft.Stack( # Stack
                                **self.dict_style('_4132'),
                                controls= [
                                    ft.Container(  # Container_Column
                                            **self.dict_style('_4139'),
                                            content= self.add_menu
                                                ), #// LAYER 1 END
                                    self.show_secundary_menu,
                    ],),),

        # ft.Container(  # Container_Column
        #     **self.dict_style('_4135'),
        #     content= ft.Column( # Column
        #             **self.dict_style('_4136'),
        #             controls= [

        #         ],
        # ),), #// CLOSE LAYER 0
        ]

        #: MAIN PHONE CONTAINER
        self.content = ft.Container(
                            **self.second_screen_style(code='MAIN_EFFECTS_CONTAINER'),
                            content = ft.Column(
                                        **self.second_screen_style(code='COLUMN_CONTAINER'),
                                        controls = self.content_box
                                        ),
                                )

        self.builder_menu_topic()

    def builder_menu_topic(self):
        # GET GIRD SCREEN SELECTED
        self.topic = GLOBAL_VAR(get_global_var='Capitulo')
        self.tmp_menu_cap = index_database.get(self.topic)
        self.check_secundary_menu = GLOBAL_VAR(get_global_var='secundary_menu_show')


        # SHOW_DICT()
        if not self.check_secundary_menu:
            for tmp_keys in self.tmp_menu_cap:
                self.builder_main_menu=  ft.Container(  # Container_Row
                                        **self.dict_style('_4143'),
                                        # on_click= lambda _: event_4143(data='_4143'),
                                        # on_click= lambda _: print(_.control.content.controls[1].content.value),
                                        on_click= lambda _: self.builder_secundary_menu(
                                                                main_widget=self.show_secundary_menu,
                                                                key_submenu=_.control.content.controls[1].content.value,
                                                                submenu=self.tmp_menu_cap.get(_.control.content.controls[1].content.value),
                                                                show_bool=False,
                                                                ),

                                        content= ft.Row( # Row
                                                **self.dict_style('_4144'),
                                                controls= [

                                                        ft.Container( # IconButton
                                                                **self.dict_style('_4147'),
                                                                # on_click= lambda _: event_4148(data='_4148'),
                                                                content= ft.IconButton(
                                                                        **self.dict_style('_4148'),
                                                                        # on_click= lambda _: event_4148(data='_4148'),
                                                                ),),

                                                        ft.Container( # Text
                                                                **self.dict_style('_4151'),
                                                                # on_click= lambda _: event_4152(data='_4152'),
                                                                content= ft.Text(
                                                                        **self.dict_style('_4152'),
                                                                        value=tmp_keys,
                                                                        # on_click= lambda _: event_4152(data='_4152'),
                                                                ),)
                                                        ],),) #// LAYER 2 END
                self.add_menu.controls.append(self.builder_main_menu)

        else:
            submenu= GLOBAL_VAR(get_global_var='Menu')
            key_sub_menu= GLOBAL_VAR(get_global_var='key_sub_menu')
            # print('hgere <===============',self.show_secundary_menu)
            self.tmp_topic = GLOBAL_VAR(get_global_var='Capitulo')
            # self.check_secundary_menu = GLOBAL_VAR(get_global_var='secundary_menu_show')

            self.builder_secundary_menu(
                                    main_widget=self.show_secundary_menu,
                                    key_submenu=key_sub_menu,
                                    submenu=submenu,
                                    show_bool=False
                                    )
            self.tmp_menu_cap_second = index_database.get(self.tmp_topic)

            for tmp_keys in self.tmp_menu_cap_second:
                self.builder_main_menu=  ft.Container(  # Container_Row
                                        **self.dict_style('_4143'),
                                        # on_click= lambda _: event_4143(data='_4143'),
                                        # on_click= lambda _: print(_.control.content.controls[1].content.value),
                                        on_click= lambda _: self.builder_secundary_menu(
                                                                main_widget=self.show_secundary_menu,
                                                                key_submenu=_.control.content.controls[1].content.value,
                                                                submenu=self.tmp_menu_cap_second.get(_.control.content.controls[1].content.value),
                                                                show_bool=True
                                                                ),

                                        content= ft.Row( # Row
                                                **self.dict_style('_4144'),
                                                controls= [

                                                        ft.Container( # IconButton
                                                                **self.dict_style('_4147'),
                                                                # on_click= lambda _: event_4148(data='_4148'),
                                                                content= ft.IconButton(
                                                                        **self.dict_style('_4148'),
                                                                        # on_click= lambda _: event_4148(data='_4148'),
                                                                ),),

                                                        ft.Container( # Text
                                                                **self.dict_style('_4151'),
                                                                # on_click= lambda _: event_4152(data='_4152'),
                                                                content= ft.Text(
                                                                        **self.dict_style('_4152'),
                                                                        value=tmp_keys,
                                                                        # on_click= lambda _: event_4152(data='_4152'),
                                                                ),)
                                                        ],),) #// LAYER 2 END
                self.add_menu.controls.append(self.builder_main_menu)

    def builder_secundary_menu(self, main_widget,key_submenu, submenu, show_bool):
        # Set main menu in second screen
        GLOBAL_VAR(
                    set_global_var={
                                'Menu':submenu,
                                # 'key_submenu':key_submenu,
                                })


        for tmp_keys in submenu:
            self.builder_submenu = ft.Container(  # Container_Row
                            **self.dict_style('_4159'),
                            on_click = lambda _: event_4159(
                                                    key_sub_menu=_.control.content.controls[1].content.value,
                                                ),

                            content = ft.Row(  # Row
                                **self.dict_style('_4160'),
                                controls = [
                                            ft.Container(  # Icon
                                                **self.dict_style('_4163'),
                                                on_click=lambda _: event_4164(secundary_main_widget=self.show_secundary_menu),
                                                content=ft.Icon(
                                                     **self.dict_style('_4164'),
                                                     # on_click= lambda _: event_4164(data='_4164'),
                                                ),),

                                            ft.Container(  # Text
                                                **self.dict_style('_4167'),
                                                # on_click= lambda _: event_4168(data='_4168'),
                                                content=ft.Text(
                                                    **self.dict_style('_4168'),
                                                    value=tmp_keys,
                                                    # on_click= lambda _: event_4168(data='_4168'),
                                                ),),
                                        ],),)  # // LAYER 2 END
            self.show_secundary_menu.content.controls.append(self.builder_submenu,)

        # SHOW
        self.show_secundary_menu.visible=True

        if show_bool:
            # show secundary menu if press back from document
            self.show_secundary_menu.update()

        secundary_menu_show = GLOBAL_VAR(get_global_var='secundary_menu_show')

        if secundary_menu_show:
            show_off = GLOBAL_VAR(get_global_var='show_off')
            if show_off == 'show_first_menu':
                self.show_secundary_menu.visible=False

        else:
            self.show_secundary_menu.update()



    def second_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)