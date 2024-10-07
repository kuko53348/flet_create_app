import flet as ft
import time


def screen_animation(widgets, animation_type):
    """
    EXEMPLE HOW USED

    type =  [
            'opacity', 'rotate', 'scale', 'rotate',
            'bounce', 'animate', 'rounded_scale'
            ]

    ft.ElevatedButton(
        text="start opacity",
        tooltip='buttom',

        on_click=lambda _:screen_animation(
                                animation_type=[
                                    'opacity',
                                    'animate',
                                    # 'scale' ,
                                    'rounded_scale',
                                    # 'bounce' ,
                                    'rotate',
                                    'shake',
                                ],
                                widgets=[
                                    tmp_effect_container_1,
                                    tmp_effect_container_2,
                                ],
                                ))
    """

    for type in animation_type:
        widget_one = widgets[0]
        widget_two = widgets[1]

        if type == "opacity":
            widget_one.opacity = 0 if widget_one.opacity == 1 else 1
            widget_two.opacity = 1 if widget_one.opacity == 0 else 0

            widget_two.update()
            widget_one.update()

        elif type == "animate":
            widget_one.offset = ft.transform.Offset(
                1.5, 0) if widget_one.offset == ft.transform.Offset(0, 0) else ft.transform.Offset(0, 0)
            widget_two.offset = ft.transform.Offset(
                1.5, 0) if widget_one.offset == ft.transform.Offset(0, 0) else ft.transform.Offset(0, 0)
            widget_two.update()
            widget_one.update()

        elif type == "rotate":
            if widget_one.rotate.angle == 490.09:
                widget_one.rotate.angle -= 490.09
                widget_two.rotate.angle += 490.09

            else:
                widget_one.rotate.angle += 490.09
                widget_two.rotate.angle -= 490.09

            widget_one.update()
            widget_two.update()

        elif type == "scale":
            widget_one.scale = 6 if not widget_one.scale == 6 else 1
            widget_two.scale = 6 if not widget_one.scale == 6 else 1
            widget_one.update()
            widget_two.update()

        elif type == "rounded_scale":
            widget_one.border_radius = ft.border_radius.all(80)
            widget_two.border_radius = ft.border_radius.all(80)
            widget_one.scale = 0 if widget_one.scale == 6 else 6
            widget_two.scale = 6 if widget_one.scale == 0 else 0
            widget_one.update()
            widget_two.update()

            time.sleep(0.6)
            widget_one.scale = 1 if widget_one.scale == 0 else 6
            widget_two.scale = 1 if widget_two.scale == 0 else 6

            widget_one.border_radius = ft.border_radius.all(16)
            widget_two.border_radius = ft.border_radius.all(16)

            widget_one.update()
            widget_two.update()

        elif type == "bounce":
            widget_one.width = 100 if widget_one.width == 150 else 150
            widget_one.height = 50 if widget_one.height == 150 else 150
            widget_one.update()

        elif type == "shake":
            widget_one.rotate.angle -= 1
            widget_two.rotate.angle += 1
            widget_one.update()
            widget_two.update()

            time.sleep(0.04)
            widget_one.rotate.angle += 2
            widget_two.rotate.angle -= 2
            widget_one.update()
            widget_two.update()

            time.sleep(0.05)
            widget_one.rotate.angle -= 1
            widget_two.rotate.angle += 1
            widget_one.update()
            widget_two.update()

