#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .doc_screen_styles import styles
from .doc_screen_events import *
from .keys_all_data_db import my_doc
from ..app_screen_db import GLOBAL_VAR

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "height": "625",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        "width": "460",
        "image": {
                'src':"fondo_doc.jpeg",
                "fit": "cover"
                },
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "padding": {"l":8,"t":8,"r":8,"b":8}
    },
    "COLUMN_CONTAINER": {
        "alignment": "center",
        "scroll": "",
        "spacing": "2",
        "tight": "false",
        "wrap": "false",
        "horizontal_alignment": "center"
    }
}

class doc_screen(ft.Container):

    def __init__(self):
        super().__init__()
        dict_keys: dict = self.doc_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):
        #: HEADER TEXT CONTAINER
        self.header_text =  ft.Text(
                                **self.dict_style('_4024'),
                                size=GLOBAL_VAR(get_global_var="text_size"),
                                value=my_doc(GLOBAL_VAR(get_global_var='documentation'))
                                # on_click= lambda _: event_4024(data='_4024'),
                                )
        #: MAIN PHONE CONTAINER
        self.content_box = [ 
                ft.Container(  # Container_Column
                    **self.dict_style('_3987'),
                    content= ft.Column( # Column
                            **self.dict_style('_3988'),
                            controls= [

                                ft.Container(  # Container_Row
                                        **self.dict_style('_3999'),
                                        content= ft.Row( # Row
                                                **self.dict_style('_4000'),
                                                controls= [

                                                        ft.Container( # IconButton
                                                                **self.dict_style('_4003'),
                                                                # on_click= lambda _: event_4004(data='_4004'),
                                                                content= ft.IconButton(
                                                                        **self.dict_style('_4004'),
                                                                        on_click= lambda _: event_4004(data='_4004'),
                                                                ),),

                                                        ft.Container( # Text
                                                                **self.dict_style('_4007'),
                                                                # on_click= lambda _: event_4008(data='_4008'),
                                                                content= ft.Text(
                                                                        **self.dict_style('_4008'),
                                                                        value=GLOBAL_VAR(get_global_var='Capitulo')
                                                                        # on_click= lambda _: event_4008(data='_4008'),
                                                                ),),

                                                        ft.Container(  # Container_Row
                                                                **self.dict_style('_4011'),
                                                                content= ft.Row( # Row
                                                                        **self.dict_style('_4012'),
                                                                        controls= [

                                                                                ft.Container( # IconButton
                                                                                        **self.dict_style('_4015'),
                                                                                        # on_click= lambda _: event_4016(data='_4016'),
                                                                                        content= ft.IconButton(
                                                                                                **self.dict_style('_4016'),
                                                                                                on_click= lambda _: event_4016(data=self.header_text),
                                                                                        ),),

                                                                                ft.Container( # IconButton
                                                                                        **self.dict_style('_4019'),
                                                                                        # on_click= lambda _: event_4020(data='_4020'),
                                                                                        content= ft.IconButton(
                                                                                                **self.dict_style('_4020'),
                                                                                                on_click= lambda _: event_4020(data=self.header_text),
                                                                                        ),),

                                                        ],),), #// LAYER 2 END
                                        ],),), #// LAYER 1 END
        ],),),
        ft.Container(  # Container_Column
            **self.dict_style('_3991'),
            content= ft.Column( # Column
                    **self.dict_style('_3992'),
                    controls= [

                        ft.Container( # Text
                                **self.dict_style('_4023'),
                                # on_click= lambda _: event_4024(data='_4024'),
                                content=self.header_text),

        ],),),
        ft.Container(  # Container_Column
            **self.dict_style('_3995'),
            content= ft.Column( # Column
                    **self.dict_style('_3996'),
                    controls= [

                ],
        ),), #// CLOSE LAYER 0
        ]

        #: MAIN PHONE CONTAINER
        self.content = ft.Container(
                            **self.doc_screen_style(code='MAIN_EFFECTS_CONTAINER'),
                            content = ft.Column(
                                        **self.doc_screen_style(code='COLUMN_CONTAINER'),
                                        controls = self.content_box
                                        ),
                                )

    def doc_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)

