
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen
from ..app_screen_db import GLOBAL_VAR
from .keys_db import index_database


# def event_4148(data): # ID: main_screen, event_Iconbutton
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Iconbutton")
#     ...

# def event_4152(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4168(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

def event_4164(secundary_main_widget): # ID: main_screen, event_Icon
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Icon")
    secundary_main_widget.content.controls.clear()
    secundary_main_widget.visible=False
    secundary_main_widget.update()

def event_4143(main_widget,sub_menu): # ID: main_screen, event_Text
    # SHOW VISIBLE SECUNDARY MENU TO READ DOC
    main_widget.visible=True
    main_widget.update()

def event_4159(key_sub_menu): # ID: main_screen, event_Text
    # SET DOCUMENTATION
    capitulo= GLOBAL_VAR(get_global_var='Capitulo')
    key_documentation= GLOBAL_VAR(get_global_var='Menu').get(key_sub_menu)
    GLOBAL_VAR(set_global_var={
                                'documentation':key_documentation,
                                })
    got_to_screen(to_screen= 'doc_screen' ,style='burble' ,time_style=0.8 )
