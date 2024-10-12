
"""
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
"""

from builder.app_manager import got_to_screen
from ..app_screen_db import GLOBAL_VAR


# def event_3992(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4016(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4004(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...

# def event_4032(data): # ID: main_screen, event_Icon
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Icon")
#     ...

# def event_4036(data): # ID: main_screen, event_Text
#     # got_to_screen(to_screen= 'screen_name' ,style='ring' ,time_style=0.8 )
#     print(f"Demo App: {data} event_Text")
#     ...
#
def event_4027(data): # ID: main_screen, event_Text
    got_to_screen(to_screen= 'first_screen' ,style='burble' ,time_style=0.8, rotation=True )
    # print(f"Demo App: {data} event_Text")
    main_page = GLOBAL_VAR(get_global_var='main_page')
