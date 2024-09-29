
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen


def event_4004(data): # ID: main_screen, event_Iconbutton
    # capitulo= GLOBAL_VAR(get_global_var='secundary_main_widget')

    got_to_screen(to_screen= 'second_screen' ,style='burble' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Iconbutton")

def event_4008(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...

def event_4016(data): # ID: main_screen, event_Iconbutton
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Iconbutton")
    data.size+=1
    data.update()

def event_4020(data): # ID: main_screen, event_Iconbutton
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    # print(f"Demo App: {data} event_Iconbutton")
    if data.size == 0:
        data.size=1
    else:
        data.size-=1

    data.update()
def event_4024(data): # ID: main_screen, event_Text
    # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
    print(f"Demo App: {data} event_Text")
    ...