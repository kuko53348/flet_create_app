#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .first_screen_styles import styles
from .first_screen_events import *

from ..app_screen_db import GLOBAL_VAR

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        # "height": "625",
        "expand":True,
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        # "width": "460",
        "image": {
                'src':"bg_first_screen.jpeg",
                "opacity": "0.22",
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
        "scroll": "HIDDEN",
        "spacing": "4",
        "horizontal_alignment": "center"
    }
}

class first_screen(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.first_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]


    def build(self):

        # print(self.data_page)

        #: MAIN PHONE CONTAINER
        self.content_box = [ 

        ft.Container(  # Container_GridView
            **self.dict_style('_3987'),
            content= ft.GridView( # GridView
                    runs_count=2,
                    **self.dict_style('_3988'),

                    controls= [

                        ft.Container(  # Container_Column
                                **self.dict_style('_3991'),
                                on_click= lambda _: event_3991(data='Capitulo 1'),

                                content= ft.Column( # Column
                                        **self.dict_style('_3992'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4067'),
                                                        # on_click= lambda _: event_4068(data='_4068'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4068'),
                                                                # on_click= lambda _: event_4068(data='_4068'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4071'),
                                                        # on_click= lambda _: event_4072(data='_4072'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4072'),
                                                                # on_click= lambda _: event_4072(data='_4072'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_3995'),
                                on_click= lambda _: event_3991(data='Capitulo 2'),

                                content= ft.Column( # Column
                                        **self.dict_style('_3996'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4035'),
                                                        # on_click= lambda _: event_4036(data='_4036'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4036'),
                                                                # on_click= lambda _: event_4036(data='_4036'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4075'),
                                                        # on_click= lambda _: event_4076(data='_4076'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4076'),
                                                                # on_click= lambda _: event_4076(data='_4076'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_3999'),
                                on_click= lambda _: event_3991(data='Capitulo 3'),
                                content= ft.Column( # Column
                                        **self.dict_style('_4000'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4039'),
                                                        # on_click= lambda _: event_4040(data='_4040'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4040'),
                                                                # on_click= lambda _: event_4040(data='_4040'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4079'),
                                                        # on_click= lambda _: event_4080(data='_4080'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4080'),
                                                                # on_click= lambda _: event_4080(data='_4080'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_4003'),
                                on_click= lambda _: event_3991(data='Capitulo 4'),

                                content= ft.Column( # Column
                                        **self.dict_style('_4004'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4043'),
                                                        # on_click= lambda _: event_4044(data='_4044'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4044'),
                                                                # on_click= lambda _: event_4044(data='_4044'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4083'),
                                                        # on_click= lambda _: event_4084(data='_4084'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4084'),
                                                                # on_click= lambda _: event_4084(data='_4084'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_4007'),
                                on_click= lambda _: event_3991(data='Capitulo 5'),

                                content= ft.Column( # Column
                                        **self.dict_style('_4008'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4047'),
                                                        # on_click= lambda _: event_4048(data='_4048'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4048'),
                                                                # on_click= lambda _: event_4048(data='_4048'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4087'),
                                                        # on_click= lambda _: event_4088(data='_4088'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4088'),
                                                                # on_click= lambda _: event_4088(data='_4088'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_4011'),
                                on_click= lambda _: event_3991(data='Capitulo 6'),

                                content= ft.Column( # Column
                                        **self.dict_style('_4012'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4051'),
                                                        # on_click= lambda _: event_4052(data='_4052'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4052'),
                                                                # on_click= lambda _: event_4052(data='_4052'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4091'),
                                                        # on_click= lambda _: event_4092(data='_4092'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4092'),
                                                                # on_click= lambda _: event_4092(data='_4092'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_4015'),
                                on_click= lambda _: event_3991(data='Capitulo 7'),

                                content= ft.Column( # Column
                                        **self.dict_style('_4016'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4055'),
                                                        # on_click= lambda _: event_4056(data='_4056'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4056'),
                                                                # on_click= lambda _: event_4056(data='_4056'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4095'),
                                                        # on_click= lambda _: event_4096(data='_4096'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4096'),
                                                                # on_click= lambda _: event_4096(data='_4096'),
                                                        ),),

                                ],),), #// LAYER 1 END
                        ft.Container(  # Container_Column
                                **self.dict_style('_4019'),
                                on_click= lambda _: event_3991(data='Capitulo 8'),

                                content= ft.Column( # Column
                                        **self.dict_style('_4020'),
                                        controls= [

                                                ft.Container( # Text
                                                        **self.dict_style('_4059'),
                                                        # on_click= lambda _: event_4060(data='_4060'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4060'),
                                                                # on_click= lambda _: event_4060(data='_4060'),
                                                        ),),

                                                ft.Container( # Text
                                                        **self.dict_style('_4099'),
                                                        # on_click= lambda _: event_4100(data='_4100'),
                                                        content= ft.Text(
                                                                **self.dict_style('_4100'),
                                                                # on_click= lambda _: event_4100(data='_4100'),
                                                        ),),

                                ],),), #// LAYER 1 END
        ],),),
        # ft.Container(  # Container_Column
        #     **self.dict_style('_4023'),
        #     content= ft.Column( # Column
        #             **self.dict_style('_4024'),
        #             controls= [

        #         ],
        # ),), #// CLOSE LAYER 0
        ]


        #: MAIN PHONE CONTAINER
        self.content = ft.Container(
                            **self.first_screen_style(code='MAIN_EFFECTS_CONTAINER'),
                            content = ft.Column(
                                        **self.first_screen_style(code='COLUMN_CONTAINER'),
                                        controls = self.content_box
                                        ),
                                )


        self.change_on_rotation()

    def change_on_rotation(self):
        # CHANGE SIZE OF WIDGET IF SCREEN IS MORE THAN ESTIMATION
        self.data_page = GLOBAL_VAR(get_global_var="main_page")
        self.data_page.on_resized=lambda _:self.change_screen(data_page=self.data_page)


    def change_screen(self,data_page):
        # CHANGE SIZE OF WIDGET IF SCREEN IS MORE THAN ESTIMATION
        self.rotation = GLOBAL_VAR(get_global_var="rotation")

        if self.rotation:
            if data_page.width >= 600: self.content_box[0].content.runs_count = 3
            else: self.content_box[0].content.runs_count = 2

            data_page.on_resized=lambda _:self.change_screen(data_page=self.data_page)
            self.content_box[0].content.update()

    def first_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)

