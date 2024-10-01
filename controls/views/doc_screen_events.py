
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen
from ..app_screen_db import GLOBAL_VAR



# def event_4008(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4024(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...
#

def event_4004(data): # ID: main_screen, event_Iconbutton
    GLOBAL_VAR(set_global_var={'secundary_menu_show':True,'show_off':'hide_first_menu'})

    got_to_screen(to_screen= 'second_screen' ,style='burble' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Iconbutton")

def event_4016(data): # ID: main_screen, event_Iconbutton
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Iconbutton")
    text_size = GLOBAL_VAR(get_global_var='text_size')
    data.size=text_size+1
    data.update()

    GLOBAL_VAR(set_global_var={'text_size':data.size})

def event_4020(data): # ID: main_screen, event_Iconbutton
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Iconbutton")
    text_size = GLOBAL_VAR(get_global_var='text_size')

    if data.size == 0:
        data.size=1
        text_size=1
    else:
        data.size=text_size - 1

    data.update()

    GLOBAL_VAR(set_global_var={'text_size':data.size})
