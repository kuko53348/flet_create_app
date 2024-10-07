
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen
from ..app_screen_db import GLOBAL_VAR


# def event_4068(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4072(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4036(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4076(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4040(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4080(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4044(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4084(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4048(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4088(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4052(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4092(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4056(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4096(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4060(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4100(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...
def event_3991(data): # ID: main_screen, event_Text
    # print(f"Demo App: {data} event_Text")

    GLOBAL_VAR(set_global_var={'Capitulo':data,'show_off':'show_first_menu','current_screen':data})
    got_to_screen(to_screen= 'second_screen' ,style='burble' ,time_style=0.8 )
